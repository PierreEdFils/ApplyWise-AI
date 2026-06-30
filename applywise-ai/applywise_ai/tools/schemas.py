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

from pydantic import BaseModel, Field
from typing import Optional, List

class AssistantInput(BaseModel):
    """Input schema for the bilingual career assistant workflow."""
    candidate_profile: Optional[str] = Field(
        None, 
        description="The candidate's resume, skills, and background."
    )
    job_posting: Optional[str] = Field(
        None, 
        description="The job description or posting details."
    )

class JobAnalysisOutput(BaseModel):
    """Output schema for the Job Analyzer Agent."""
    job_title: str = Field(description="The title of the job posting.")
    company_name: str = Field(description="The name of the company hiring.")
    location: str = Field(description="The job location.")
    work_mode: str = Field(description="The work mode (e.g., Remote, Hybrid, On-site).")
    seniority_level: str = Field(description="The seniority level of the position (e.g., Senior, Mid, Junior).")
    main_responsibilities: List[str] = Field(description="List of the main responsibilities of the role.")
    required_skills: List[str] = Field(description="List of required skills.")
    preferred_skills: List[str] = Field(description="List of preferred skills.")
    important_keywords: List[str] = Field(description="List of important keywords from the posting.")
    tools_and_technologies: List[str] = Field(description="List of tools and technologies mentioned.")
    language_requirements: str = Field(description="Language requirements (e.g., English, French, Bilingual).")

class CandidateFitOutput(BaseModel):
    """Output schema for the Candidate Fit Agent."""
    fit_assessment: str = Field(description="The detailed candidate fit assessment report in markdown.")

class ResumeTailoringOutput(BaseModel):
    """Output schema for the Resume Tailor Agent."""
    tailored_resume: str = Field(description="The tailored resume recommendations and bullet points in markdown.")

class InterviewPrepOutput(BaseModel):
    """Output schema for the Interview Coach Agent."""
    prep_guide: str = Field(description="The interview preparation questions, tips, and guidelines in markdown.")

class FinalPackageOutput(BaseModel):
    """Output schema for the Root Orchestrator's final application package."""
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
