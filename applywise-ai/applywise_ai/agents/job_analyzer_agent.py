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
from google.adk.models import Gemini
from google.genai import types

from ..tools.schemas import JobAnalysisOutput

# Responsible for reading the job posting and extracting structured information
job_analyzer = Agent(
    name="job_analyzer",
    model=Gemini(
        model="gemini-2.5-flash",
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""
    You are an expert Canadian Tech Recruiter and Job Analyst.
    Analyze the provided job posting: {job_posting}
    
    You must extract and populate all 11 fields in the output schema:
    1. job_title: The title of the job.
    2. company_name: The name of the hiring company.
    3. location: The location of the job.
    4. work_mode: The work mode (Remote, Hybrid, On-site).
    5. seniority_level: The seniority level (Senior, Mid, Junior, Entry).
    6. main_responsibilities: List of the main responsibilities.
    7. required_skills: List of required skills.
    8. preferred_skills: List of preferred skills.
    9. important_keywords: List of important keywords from the posting.
    10. tools_and_technologies: List of tools, software, or technologies mentioned.
    11. language_requirements: Language requirements (e.g., English, French, Bilingual).
    
    Ensure that the extraction is precise and highly structured.
    """,
    output_schema=JobAnalysisOutput,
    output_key="job_analysis"
)
