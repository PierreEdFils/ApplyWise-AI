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

from google.adk.workflow import Workflow, START
from typing import Union

from ..tools.schemas import AssistantInput, FinalPackageOutput
from ..tools.nodes import check_inputs, ask_for_inputs
from ..agents.root_agent import root_orchestrator

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
