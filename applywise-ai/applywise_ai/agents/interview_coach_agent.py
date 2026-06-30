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

from ..tools.schemas import InterviewPrepOutput

# Responsible for generating interview preparation guidelines, questions, and pitches
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
    output_key="interview_prep",
)
