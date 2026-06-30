import os
import sys
from google.adk.agents import Agent, SequentialAgent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

# Resolve absolute path to the local MCP server
mcp_server_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "mcp_server.py"))

# Configure Stdio connection to run the MCP server using the current Python interpreter
connection_params = StdioConnectionParams(
    server_params=StdioServerParameters(
        command=sys.executable,
        args=[mcp_server_path],
    )
)

# Load the MCP toolset
mcp_toolset = McpToolset(connection_params=connection_params)

# Get default model from environment or fallback to gemini-2.5-flash
DEFAULT_MODEL = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")

# --- 1. JOB ANALYZER AGENT ---
job_analyzer_agent = Agent(
    name="job_analyzer",
    model=DEFAULT_MODEL,
    instruction="""
    You are the Job Analyzer Agent. Your task is to analyze the job description provided in {job_description}.
    
    1. Extract the following metadata:
       - Job Title
       - Company Name
       - Location
       - Seniority Level (e.g., Junior, Mid, Senior)
       - Work Mode (e.g., Remote, Hybrid, On-site)
    2. Extract key responsibilities as a bulleted list.
    3. Identify required technical and soft skills.
    4. Use the `extract_keywords` tool on the job description to get a standardized list of key technical terms.
    
    Format your final response as a clean markdown structure. Save your output in the state.
    """,
    tools=[mcp_toolset],
    output_key="job_analysis"
)

# --- 2. CANDIDATE FIT AGENT ---
candidate_fit_agent = Agent(
    name="candidate_fit",
    model=DEFAULT_MODEL,
    instruction="""
    You are the Candidate Fit Agent. Your task is to compare the candidate profile in {candidate_profile} to the job analysis in {job_analysis}.
    
    1. Extract keywords from the candidate profile using the `extract_keywords` tool.
    2. Compare the candidate's keywords to the job's keywords using the `calculate_match_score` and `detect_missing_skills` tools.
    3. Produce:
       - A match score (an integer 0-100)
       - Key strengths (where the candidate's profile matches the job requirements)
       - Critical gaps (missing skills or experience)
       - Positioning advice (how the candidate should present themselves to bridge the gaps)
       
    Format your final response in clean markdown. Save your output in the state.
    """,
    tools=[mcp_toolset],
    output_key="candidate_fit"
)

# --- 3. RESUME TAILOR AGENT ---
resume_tailor_agent = Agent(
    name="resume_tailor",
    model=DEFAULT_MODEL,
    instruction="""
    You are the Resume Tailor Agent. Your task is to customize the candidate's resume based on the candidate profile in {candidate_profile} and the job analysis in {job_analysis}.
    
    Generate:
    1. A tailored, attention-grabbing Resume Headline.
    2. A professional Resume Summary (2-3 sentences) optimized for the target role.
    3. A Skills Section categorizing key matching skills.
    4. 3-4 tailored Achievement-based Resume Bullet Points. For each bullet point, use the `format_resume_bullet` tool to structure it using the Google formula (Accomplished [X], measured by [Y], by doing [Z]).
    
    Format your final response in clean markdown. Save your output in the state.
    """,
    tools=[mcp_toolset],
    output_key="resume_tailoring"
)

# --- 4. INTERVIEW COACH AGENT ---
interview_coach_agent = Agent(
    name="interview_coach",
    model=DEFAULT_MODEL,
    instruction="""
    You are the Interview Coach Agent. Your task is to prepare the candidate for interviews based on the candidate profile in {candidate_profile} and the job analysis in {job_analysis}.
    
    Generate:
    1. 3 likely Interview Questions (behavioral and technical).
    2. A STAR answer outline (Situation, Task, Action, Result) for each question.
    3. Technical Prep Notes highlighting core concepts the candidate should review.
    4. A 30-second English Elevator Pitch.
    5. A 30-second French Elevator Pitch.
    
    Format your final response in clean markdown. Save your output in the state.
    """,
    tools=[mcp_toolset],
    output_key="interview_coaching"
)

# --- 5. ROOT ORCHESTRATOR ---
# SequentialAgent chains all four sub-agents together.
# State from previous agents is automatically passed down the pipeline.
root_orchestrator = SequentialAgent(
    name="applywise_orchestrator",
    sub_agents=[
        job_analyzer_agent,
        candidate_fit_agent,
        resume_tailor_agent,
        interview_coach_agent
    ]
)
