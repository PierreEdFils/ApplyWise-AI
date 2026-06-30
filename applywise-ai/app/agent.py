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
from typing import Optional

from google.adk.workflow import Workflow, node, START
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.events.event import Event
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

# Define output schemas for the agents to ensure structured and reliable data flow
class JobAnalysisOutput(BaseModel):
    analysis: str = Field(description="The detailed job analysis report in markdown.")

class CandidateFitOutput(BaseModel):
    fit_assessment: str = Field(description="The detailed candidate fit assessment report in markdown.")

class ResumeTailoringOutput(BaseModel):
    tailored_resume: str = Field(description="The tailored resume recommendations and bullet points in markdown.")

class InterviewPrepOutput(BaseModel):
    prep_guide: str = Field(description="The interview preparation questions, tips, and guidelines in markdown.")

class FinalPackageOutput(BaseModel):
    complete_package: str = Field(description="The consolidated, bilingual Canadian Tech Application Package in markdown.")

# 1. Input Checker Node
@node
def check_inputs(node_input: AssistantInput) -> Event:
    profile = node_input.candidate_profile
    job = node_input.job_posting
    
    # Verify both inputs exist and have reasonable content length
    if not profile or not job or len(profile.strip()) < 15 or len(job.strip()) < 15:
        return Event(output=node_input, route="missing")
    
    # Store inputs in the session state so subsequent agents can access them
    return Event(
        output=node_input,
        route="valid",
        state={
            "candidate_profile": profile,
            "job_posting": job
        }
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

# 6. Root Orchestrator Agent
root_orchestrator = Agent(
    name="root_orchestrator",
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""
    You are the Lead Career Coach and Orchestrator.
    Compile and synthesize the outputs from all previous stages:
    - Job Analysis: {job_analysis}
    - Candidate Fit: {candidate_fit}
    - Tailored Resume Recommendations: {tailored_resume}
    - Interview Prep Guide: {interview_prep}
    
    Generate a complete, professionally formatted "Canadian Tech Application Package".
    The package must be highly encouraging, structured with clear markdown headings, and include bilingual (English and French) sections where appropriate or a bilingual summary.
    """,
    output_schema=FinalPackageOutput
)

# 7. Fallback Node for Missing/Unrelated Inputs
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

# Define the graph workflow edges using the correct tuple-based RoutingMap syntax
edges = [
    (START, check_inputs),
    (check_inputs, {
        "valid": job_analyzer,
        "missing": ask_for_inputs
    }),
    (job_analyzer, candidate_fit_agent, resume_tailor, interview_coach, root_orchestrator)
]

# Define the root workflow agent
root_agent = Workflow(
    name="applywise_ai",
    edges=edges,
    input_schema=AssistantInput,
    description="Bilingual career application assistant for Canadian tech job seekers."
)

# Initialize the App container
app = App(
    root_agent=root_agent,
    name="app",
)
