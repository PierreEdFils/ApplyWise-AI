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

from ..tools.schemas import ResumeTailoringOutput

# Responsible for generating tailored resume content and a cover letter draft
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
    output_key="tailored_resume",
)
