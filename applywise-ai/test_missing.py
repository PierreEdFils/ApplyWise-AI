import asyncio
import sys

from google.adk.apps import App
from google.adk.runners import InMemoryRunner
from google.genai import types

# Force UTF-8 encoding on stdout for Windows console compatibility
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# Initialize GCP environment and import the workflow root agent
import applywise_ai.config  # noqa: F401
from applywise_ai.workflow.graph import root_agent


async def main():
    app = App(name="app", root_agent=root_agent)
    runner = InMemoryRunner(app=app)
    session = await runner.session_service.create_session(
        app_name="app", user_id="test_user"
    )

    print("--- Running Workflow with Missing Inputs ---")
    # Sending missing inputs (only candidate profile, no job posting)
    async for event in runner.run_async(
        user_id="test_user",
        session_id=session.id,
        new_message=types.Content(
            role="user",
            parts=[
                types.Part.from_text(
                    text='{"candidate_profile": "Senior Software Engineer"}'
                )
            ],
        ),
    ):
        if event.content is not None and event.content.parts is not None:
            # Print content parts
            for part in event.content.parts:
                if part.text:
                    print(part.text)
        if event.output is not None:
            print(f"\nFinal Output: {event.output}")


if __name__ == "__main__":
    asyncio.run(main())
