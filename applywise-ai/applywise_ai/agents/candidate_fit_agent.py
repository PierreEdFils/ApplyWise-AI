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

from ..tools.schemas import CandidateFitOutput

# Responsible for comparing the candidate's profile against the job analysis
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
    output_key="candidate_fit",
)
