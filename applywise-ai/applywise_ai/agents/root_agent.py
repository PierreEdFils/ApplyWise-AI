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

from google.adk.agents import Agent
from google.adk.agents.context import Context
from google.adk.models import Gemini
from google.adk.workflow import node
from google.genai import types

from ..tools.schemas import AssistantInput, FinalPackageOutput
from .candidate_fit_agent import candidate_fit_agent
from .interview_coach_agent import interview_coach
from .job_analyzer_agent import job_analyzer
from .resume_tailor_agent import resume_tailor

# Compiler Agent responsible for consolidating and formatting the final 11-field output package
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
    output_key="final_package",
)


@node(rerun_on_resume=True)
async def root_orchestrator(
    ctx: Context, node_input: AssistantInput
) -> FinalPackageOutput:
    """The Root Orchestrator Agent that controls the full multi-agent workflow.

    It receives the candidate profile and job posting, updates the state,
    and programmatically routes to each sub-agent before compiling the results.
    """
    # Set the candidate profile and job posting in the state so all sub-agents can access them
    ctx.state["candidate_profile"] = node_input.candidate_profile
    ctx.state["job_posting"] = node_input.job_posting

    # 1. Run Job Analyzer Agent
    job_analysis = await ctx.run_node(job_analyzer, node_input=node_input.job_posting)
    ctx.state["job_analysis"] = job_analysis

    # 2. Run Candidate Fit Agent
    candidate_fit = await ctx.run_node(
        candidate_fit_agent, node_input=node_input.candidate_profile
    )
    ctx.state["candidate_fit"] = candidate_fit.get("fit_assessment", "")

    # 3. Run Resume Tailor Agent
    resume_tailored = await ctx.run_node(
        resume_tailor, node_input=node_input.candidate_profile
    )
    ctx.state["tailored_resume"] = resume_tailored.get("tailored_resume", "")

    # 4. Run Interview Coach Agent
    interview_prep = await ctx.run_node(
        interview_coach, node_input=node_input.candidate_profile
    )
    ctx.state["interview_prep"] = interview_prep.get("prep_guide", "")

    # 5. Run Compiler Agent to produce the final structured application package
    final_package = await ctx.run_node(
        compiler_agent, node_input="Please compile the application package."
    )

    return final_package
