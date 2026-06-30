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

"""ADK entry point — kept minimal.

All agent logic lives in the ``applywise_ai`` package.
This file exists because the ADK CLI expects ``app/agent.py``.
"""

from google.adk.apps import App

import applywise_ai.config  # noqa: F401  — triggers GCP env init
from applywise_ai.workflow.graph import root_agent

# Initialize the App container
app = App(
    root_agent=root_agent,
    name="app",
)
