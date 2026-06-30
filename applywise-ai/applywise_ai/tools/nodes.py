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

from google.adk.workflow import node
from google.adk.events.event import Event
from google.genai import types

from .schemas import AssistantInput

@node
def check_inputs(node_input: AssistantInput) -> Event:
    """Verifies that both candidate profile and job posting are provided with sufficient length."""
    profile = node_input.candidate_profile
    job = node_input.job_posting
    
    if not profile or not job or len(profile.strip()) < 15 or len(job.strip()) < 15:
        return Event(output=node_input, route="missing")
    
    return Event(
        output=node_input,
        route="valid"
    )

@node
def ask_for_inputs(node_input: AssistantInput) -> Event:
    """Fallback node that politely asks the user to provide both required inputs."""
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
