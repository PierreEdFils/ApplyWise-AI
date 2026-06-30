# ruff: noqa
# Copyright 2026 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import google.auth
from pydantic import BaseModel, Field
from typing import Optional, List, Union

from google.adk.workflow import Workflow, node, START
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.events.event import Event
from google.adk.agents.context import Context
from google.adk.models import Gemini
from google.genai import types

# Set up Google Cloud project environment variables
_, project_id = google.auth.default()
os.environ["GOOGLE_CLOUD_PROJECT"] = project_id
os.environ["GOOGLE_CLOUD_LOCATION"] = "global"
os.environ["GOOGLE_GENAI_USE_VERTEXAI"] = "True"

# Define the input schema for the workflow
class AssistantInput(BaseModel):
    candidate_profile: Optional[str] = Field(
        None, 
        description="The candidate's resume, skills, and background."
    )
    job_posting: Optional[str] = Field(
        None, 
        description="The job description or posting details."
    )

# Define output schemas for intermediate agents to ensure structured data flow
class JobAnalysisOutput(BaseModel):
    analysis: str = Field(description="The detailed job analysis report in markdown.")

class CandidateFitOutput(BaseModel):
    fit_assessment: str = Field(description="The detailed candidate fit assessment report in markdown.")

class ResumeTailoringOutput(BaseModel):
    tailored_resume: str = Field(description="The tailored resume recommendations and bullet points in markdown.")

class InterviewPrepOutput(BaseModel):
    prep_guide: str = Field(description="The interview preparation questions, tips, and guidelines in markdown.")

# The final consolidated application package schema requested by the user
class FinalPackageOutput(BaseModel):
    job_summary: str = Field(description="A concise summary of the job role and company.")
    match_score: int = Field(description="A candidate fit score out of 100 based on the fit analysis.")
    top_matching_skills: List[str] = Field(description="List of the candidate's skills that match the job requirements.")
    missing_skills: List[str] = Field(description="List of key skills or requirements the candidate is missing.")
    resume_headline: str = Field(description="A professional, tailored resume headline.")
    professional_summary: str = Field(description="A tailored professional summary (bilingual: English & French).")
    resume_bullet_points: List[str] = Field(description="3-5 tailored achievement-oriented bullet points for the resume (bilingual: English & French).")
    cover_letter_draft: str = Field(description="A drafted cover letter tailored to the job posting (bilingual: English & French).")
    interview_questions: List[str] = Field(description="3-4 likely interview questions and preparation tips.")
    bilingual_pitch: str = Field(description="A 30-second elevator pitch in both English and French.")
    application_checklist: List[str] = Field(description="A checklist of next steps for the candidate.")

# 1. Input Checker Node
@node
def check_inputs(node_input: AssistantInput) -> Event:
    profile = node_input.candidate_profile
    job = node_input.job_posting
    
    # Verify both inputs exist and have reasonable content length
    if not profile or not job or len(profile.strip()) < 15 or len(job.strip()) < 15:
        return Event(output=node_input, route="missing")
    
    return Event(
        output=node_input,
        route="valid"
    )

# 2. Job Analyzer Agent
job_analyzer = Agent(
    name="job_analyzer",
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""
    You are an expert Canadian Tech Recruiter and Job Analyst.
    Analyze the provided job posting: {job_posting}
    
    Identify and extract:
    1. Core technical skills, programming languages, and frameworks required.
    2. Essential soft skills, methodologies (e.g., Agile, DevOps), and cultural fit.
    3. Canadian tech market context (e.g., location, remote/hybrid norms, potential bilingual requirements).
    
    If the job posting is in French, perform the analysis and output the result in both English and French.
    """,
    output_schema=JobAnalysisOutput,
    output_key="job_analysis"
)

# 3. Candidate Fit Agent
candidate_fit_agent = Agent(
    name="candidate_fit",
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""
    You are a Career Consultant specializing in the Canadian tech sector.
    Compare the candidate's profile: {candidate_profile} against the Job Analysis: {job_analysis}
    
    Provide a detailed assessment:
    1. Key Strengths: Where does the candidate strongly align with the job requirements?
    2. Gap Analysis: What critical technical or soft skills is the candidate missing or lacking depth in?
    3. Actionable Recommendations: How can the candidate address these gaps in their application or interview?
    
    Provide the feedback in a constructive, bilingual-friendly tone.
    """,
    output_schema=CandidateFitOutput,
    output_key="candidate_fit"
)

# 4. Resume Tailor Agent
resume_tailor = Agent(
    name="resume_tailor",
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""
    You are an expert Resume Writer for the Canadian tech market.
    Using the candidate's profile: {candidate_profile}, the Job Analysis: {job_analysis}, and the Fit Assessment: {candidate_fit}, generate:
    
    1. A tailored professional summary (approx. 3-4 sentences) highlighting their fit.
    2. 3-5 tailored achievement-oriented bullet points for their most recent experience following Canadian resume best practices (action verbs, quantifiable impact, no photos or personal info).
    3. Recommendations for adjusting their skills section.
    
    If the job requires bilingualism or is located in a bilingual region (e.g., Ottawa, Montreal), provide tailored content in both English and French.
    """,
    output_schema=ResumeTailoringOutput,
    output_key="tailored_resume"
)

# 5. Interview Coach Agent
interview_coach = Agent(
    name="interview_coach",
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""
    You are a Tech Interview Coach.
    Based on the Job Analysis: {job_analysis} and the Candidate's Profile: {candidate_profile}, generate:
    
    1. 3-4 likely technical or behavioral interview questions (using the STAR method) specific to this role.
    2. Clear guidance on how the candidate should answer them using their background.
    3. A brief bilingual (English/French) tip sheet for interviewing in the Canadian tech landscape (cultural expectations, discussing work authorization, bilingual communication).
    """,
    output_schema=InterviewPrepOutput,
    output_key="interview_prep"
)

# 6. Compiler Agent
compiler_agent = Agent(
    name="compiler_agent",
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""
    You are the Lead Career Coach and Compiler.
    You will receive:
    - Job Analysis: {job_analysis}
    - Candidate Fit: {candidate_fit}
    - Tailored Resume: {tailored_resume}
    - Interview Prep: {interview_prep}
    - Candidate Profile: {candidate_profile}
    - Job Posting: {job_posting}
    
    Compile these into a structured, bilingual (English/French) Canadian Tech Application Package.
    
    You must populate all 11 fields in the output schema:
    1. job_summary: A concise summary of the job role and company.
    2. match_score: A candidate fit score out of 100 based on the fit analysis.
    3. top_matching_skills: List of the candidate's skills that match the job requirements.
    4. missing_skills: List of key skills or requirements the candidate is missing.
    5. resume_headline: A professional, tailored resume headline.
    6. professional_summary: A tailored professional summary (bilingual: English & French).
    7. resume_bullet_points: 3-5 tailored achievement-oriented bullet points for the resume (bilingual: English & French).
    8. cover_letter_draft: A drafted cover letter tailored to the job posting (bilingual: English & French).
    9. interview_questions: 3-4 likely interview questions and preparation tips.
    10. bilingual_pitch: A 30-second elevator pitch in both English and French.
    11. application_checklist: A checklist of next steps for the candidate.
    """,
    output_schema=FinalPackageOutput,
    output_key="final_package"
)

# 7. Dynamic Orchestrator Node
@node(rerun_on_resume=True)
async def root_orchestrator(ctx: Context, node_input: AssistantInput) -> FinalPackageOutput:
    # Set the candidate profile and job posting in the state so all sub-agents can access them
    ctx.state["candidate_profile"] = node_input.candidate_profile
    ctx.state["job_posting"] = node_input.job_posting

    # 1. Run Job Analyzer Agent
    job_analysis = await ctx.run_node(job_analyzer, node_input=node_input.job_posting)
    ctx.state["job_analysis"] = job_analysis.get("analysis", "")

    # 2. Run Candidate Fit Agent
    candidate_fit = await ctx.run_node(candidate_fit_agent, node_input=node_input.candidate_profile)
    ctx.state["candidate_fit"] = candidate_fit.get("fit_assessment", "")

    # 3. Run Resume Tailor Agent
    resume_tailored = await ctx.run_node(resume_tailor, node_input=node_input.candidate_profile)
    ctx.state["tailored_resume"] = resume_tailored.get("tailored_resume", "")

    # 4. Run Interview Coach Agent
    interview_prep = await ctx.run_node(interview_coach, node_input=node_input.candidate_profile)
    ctx.state["interview_prep"] = interview_prep.get("prep_guide", "")

    # 5. Run Compiler Agent to produce the final structured application package
    final_package = await ctx.run_node(compiler_agent, node_input="Please compile the application package.")
    
    return final_package

# 8. Fallback Node for Missing/Unrelated Inputs
@node
def ask_for_inputs(node_input: AssistantInput) -> Event:
    msg = (
        "Bonjour! Hello! Welcome to the Canadian Tech Career Application Assistant. 🍁\n\n"
        "To help you tailor your application, please provide both:\n"
        "1. Your **Candidate Profile** (resume, skills, experience)\n"
        "2. The **Job Posting** (job description, requirements)\n\n"
        "Please paste them in your next message so we can get started!"
    )
    return Event(
        content=types.Content(role="model", parts=[types.Part.from_text(text=msg)]),
        output=msg
    )

# Define the graph workflow edges
edges = [
    (START, check_inputs),
    (check_inputs, {
        "valid": root_orchestrator,
        "missing": ask_for_inputs
    })
]

# Define the root workflow agent
root_agent = Workflow(
    name="applywise_ai",
    edges=edges,
    input_schema=AssistantInput,
    output_schema=Union[FinalPackageOutput, str],
    description="Bilingual career application assistant for Canadian tech job seekers."
)

# Initialize the App container
app = App(
    root_agent=root_agent,
    name="app",
)
