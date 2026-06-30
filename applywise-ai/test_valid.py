import asyncio
import sys
from google.adk.apps import App
from google.adk.runners import InMemoryRunner
from google.genai import types

# Force UTF-8 encoding on stdout for Windows console compatibility
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding='utf-8')

# Add the app directory to path
sys.path.append(".")
from app.agent import root_agent

async def main():
    app = App(name="app", root_agent=root_agent)
    runner = InMemoryRunner(app=app)
    session = await runner.session_service.create_session(
        app_name="app", user_id="test_user"
    )
    
    candidate_profile = """
    Pierre Ed Fils
    Senior Fullstack Software Engineer
    Location: Montreal, QC (Bilingual: English & French)
    Experience:
    - 5 years at TechCorp building scalable web applications.
    - Proficient in Python (FastAPI, Django), React, TypeScript, and Google Cloud Platform (GCP).
    - Designed and implemented microservices on GKE and Cloud Run.
    - Led a team of 3 developers to migrate a legacy system, improving performance by 40%.
    """
    
    job_posting = """
    Senior Fullstack Developer (Bilingual English/French)
    Company: ApplyWise AI
    Location: Ottawa, ON (Hybrid)
    Requirements:
    - 5+ years of experience in fullstack web development.
    - Strong proficiency in Python (FastAPI/Flask) and React/TypeScript.
    - Experience with cloud platforms (GCP preferred).
    - Excellent communication skills; bilingualism (English/French) is highly preferred for collaborating with teams in Quebec and Ontario.
    - Passion for AI and building next-gen developer tools.
    """
    
    import json
    input_data = json.dumps({
        "candidate_profile": candidate_profile,
        "job_posting": job_posting
    })
    
    print("--- Running Workflow with Valid Inputs ---")
    async for event in runner.run_async(
        user_id="test_user",
        session_id=session.id,
        new_message=types.Content(
            role="user", 
            parts=[types.Part.from_text(text=input_data)]
        ),
    ):
        # Print intermediate outputs and content as they arrive
        if event.content is not None:
            for part in event.content.parts:
                if part.text:
                    print(part.text, end="", flush=True)
        if event.output is not None:
            print(f"\n\n[Final Output Object]:\n{event.output}")

if __name__ == "__main__":
    asyncio.run(main())
