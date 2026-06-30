import streamlit as st
import asyncio
import os
import sys
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set Streamlit page config
st.set_page_config(
    page_title="ApplyWise AI | Bilingual Career Agent",
    page_icon="🇨🇦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Premium CSS for styling
st.markdown("""
<style>
    /* Main Background & Text */
    .stApp {
        background-color: #080C15;
        color: #F3F4F6;
    }
    
    /* Sidebar styling */
    section[data-testid="stSidebar"] {
        background-color: #0F1626;
        border-right: 1px solid rgba(255, 255, 255, 0.07);
    }
    
    /* Headings */
    h1, h2, h3, h4 {
        font-family: 'Outfit', sans-serif;
        font-weight: 700;
    }
    
    .text-gradient {
        background: linear-gradient(135deg, #00F2FE 0%, #9B5DE5 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
    }
    
    /* Metric Cards */
    .metric-card {
        background-color: rgba(20, 29, 47, 0.65);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        margin-bottom: 20px;
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 800;
        color: #00F2FE;
    }
    
    /* Paper sheet styling for Cover Letter */
    .paper-container {
        background-color: #FFFFFF;
        color: #1F2937;
        padding: 40px;
        border-radius: 8px;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.5);
        font-family: 'Georgia', serif;
        font-size: 1rem;
        line-height: 1.6;
        white-space: pre-wrap;
        border: 1px solid rgba(0, 0, 0, 0.05);
    }
    
    /* Tabs styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 6px 6px 0px 0px;
        padding: 8px 16px;
        color: #9CA3AF;
    }
    
    .stTabs [aria-selected="true"] {
        background-color: rgba(0, 242, 254, 0.1) !important;
        border-color: #00F2FE !important;
        color: #00F2FE !important;
    }
</style>
""", unsafe_allow_html=True)

# --- PRESET DEMO DATA ---
PRESET_JOBS = {
    "Shopify - Bilingual Developer": """About the Role:
Shopify is looking for a Bilingual Full-Stack Developer to join our merchant experience team. You will work on building scalable web applications that power millions of merchants globally.

Key Responsibilities:
- Design and develop highly interactive web frontends using React, TypeScript, and modern state management.
- Build robust, scalable backend APIs using Ruby on Rails and PostgreSQL.
- Collaborate with product managers, designers, and other engineering teams.
- Support our bilingual merchant base (English and French).

Requirements:
- 3+ years of experience in full-stack web development.
- Strong proficiency in React/JavaScript and Ruby on Rails.
- Experience with RESTful APIs, GraphQL, and relational databases.
- Strong communication skills in English and French (bilingual proficiency).""",
    "Coveo - Senior DevOps Engineer": """About Coveo:
Coveo is looking for a Senior DevOps & Cloud Engineer to join our infrastructure team in Montreal.

Key Responsibilities:
- Manage, scale, and optimize our global AWS cloud infrastructure.
- Orchestrate containerized microservices using Kubernetes (EKS).
- Build and maintain robust CI/CD pipelines (GitLab CI, Terraform).
- French Language Requirement: Team collaboration and technical meetings are primarily conducted in French. Professional French proficiency is imperative.

Requirements:
- 5+ years of DevOps/Cloud engineering experience.
- Strong expertise with AWS, Terraform, and Kubernetes.
- Professional level fluency in French is required."""
}

PRESET_CANDIDATES = {
    "Shopify - Bilingual Developer": """Jean-Pierre Tremblay
Ottawa, ON | jp.tremblay@email.com | (613) 555-0199

Summary:
Full-Stack Developer with 4 years of experience building web applications. Highly proficient in React, JavaScript, and Node.js. Intermediate communication skills in French, seeking to transition into a bilingual technical role.

Experience:
Web Developer | TechNorth Solutions, Toronto (Remote) | 2022 - Present
- Built and maintained client-facing dashboards using React and Redux, improving load times by 20%.
- Developed backend microservices using Node.js, Express, and MongoDB.

Education & Skills:
- B.Sc. in Computer Science | Carleton University, Ottawa
- Languages: English (Fluent), French (Intermediate/B2)
- Tech: React, Node.js, Express, PostgreSQL, Git, Agile""",
    "Coveo - Senior DevOps Engineer": """Sarah Jenkins
Montreal, QC | sarah.jenkins@email.com

Summary:
Senior DevOps Engineer with 6 years of experience specializing in cloud infrastructure automation, Kubernetes orchestration, and CI/CD pipelines. Native English speaker with working proficiency in French.

Experience:
Cloud Infrastructure Engineer | CloudScale Inc., Vancouver (Remote) | 2021 - Present
- Automated AWS infrastructure provisioning using Terraform, reducing deployment times by 40%.
- Managed production Kubernetes clusters (EKS) hosting 50+ microservices.

Skills:
AWS, Kubernetes, Terraform, Docker, Python, Bash, CI/CD, Git
Languages: English (Native), French (Intermediate)"""
}

# --- SIMULATED CAPSTONE OUTPUTS ---
SIMULATED_OUTPUTS = {
    "Shopify - Bilingual Developer": {
        "job_analysis": """### 📋 Job Analysis Summary
- **Job Title**: Bilingual Full-Stack Developer
- **Company**: Shopify
- **Location**: Ottawa, ON (Hybrid/Remote)
- **Seniority Level**: Mid-to-Senior (3+ years)
- **Work Mode**: Hybrid / Remote

### 🔑 Key Required Skills
- **Frontend**: React, TypeScript, Modern State Management
- **Backend**: Ruby on Rails, PostgreSQL
- **APIs & Data**: RESTful APIs, GraphQL, Relational Databases
- **Language**: Bilingual Proficiency (English and French)""",
        
        "candidate_fit": """### 📊 Candidate Fit Analysis
- **Overall Match Score**: **78 / 100**
- **Strong Matching Experience**:
  - 4 years of Full-Stack experience (exceeds the 3-year requirement).
  - Strong proficiency in React and JavaScript.
  - Relational database experience with PostgreSQL.
- **Missing Skills / Gaps**:
  - No professional experience with **Ruby on Rails** (profile shows Node.js/Express).
  - **French Language**: Candidate is Intermediate (B2), but the role requires bilingual proficiency.
- **Positioning Advice**:
  - Emphasize strong JavaScript/Node.js backend foundations to demonstrate ability to learn Ruby on Rails quickly.
  - Highlight willingness to undergo bilingual technical training.""",
        
        "resume_tailoring": """### 📄 Tailored Resume Assets
- **Tailored Resume Headline**:
  > *Bilingual Full-Stack Developer | 4+ Years Experience | React & Node.js Specialist (Ruby on Rails transitioning)*
- **Professional Resume Summary**:
  > *Versatile Full-Stack Developer with 4 years of experience specializing in high-performance React frontends and scalable backend architectures. Fully bilingual in English and French, with proven success optimizing merchant dashboards and collaborating in Agile product environments.*
- **Tailored Resume Bullet Points**:
  - **Optimized** client-facing dashboards using React and Redux, resulting in a **20% improvement in page load times**.
  - **Architected** scalable payment microservices using Node.js, Express, and PostgreSQL, resulting in **35% faster developer onboarding**.
  - **Collaborated** in bilingual Agile Scrum teams, facilitating daily standups and sprint planning in both **English and French**.""",
        
        "interview_coaching": """### 💬 Interview Coaching & Pitches
#### 1. Likely Interview Questions & STAR Outlines:
- **Q1 (Technical)**: Shopify uses Ruby on Rails. How do you plan to transition from Node.js?
  - *STAR Outline*:
    - **S**: In my previous role, our backend was built entirely on Node.js.
    - **T**: I need to transition to Rails for Shopify's ecosystem.
    - **A**: I have already built prototype MVC applications in Rails, leveraging my strong SQL and MVC patterns.
    - **R**: This allows me to ramp up and start committing code within my first two weeks.
- **Q2 (Bilingual)**: Pouvez-vous me parler d'une situation où vous avez dû collaborer en français?
  - *STAR Outline*:
    - **S**: Chez TechNorth, nous avions des marchands francophones au Québec.
    - **T**: Il fallait traduire nos spécifications techniques.
    - **A**: J'ai animé des sessions de cadrage en français pour recueillir leurs besoins.
    - **R**: Ce qui a permis de livrer une interface parfaitement adaptée.

#### 2. Elevator Pitches:
- **English Pitch**:
  > *Hi, I'm Jean-Pierre. I'm a Full-Stack Developer with 4 years of experience specializing in React and Node.js. I have a proven track record of optimizing dashboard performance and building scalable APIs. I'm excited to bring my React expertise to Shopify and rapidly transition my backend skills to Ruby on Rails.*
- **French Pitch**:
  > *Bonjour, je m'appelle Jean-Pierre. Je suis développeur Full-Stack avec 4 ans d'expérience. Je maîtrise React et les architectures d'API. Habitant à Ottawa, je travaille couramment en anglais et en français, ce qui me permet de collaborer efficacement avec vos équipes et vos marchands bilingues.*""",
        
        "cover_letter": """Jean-Pierre Tremblay
Ottawa, ON | jp.tremblay@email.com
June 30, 2026

Hiring Team
Shopify
Ottawa, ON

Subject: Application for Bilingual Full-Stack Developer Role

Dear Shopify Hiring Team,

I am writing to express my enthusiastic interest in the Bilingual Full-Stack Developer position at Shopify. With four years of professional experience building responsive web applications, a deep specialization in React, and professional bilingual proficiency in English and French, I am excited to help Shopify power commerce for millions of merchants worldwide.

In my previous role at TechNorth Solutions, I focused on developing high-performance user interfaces using React and Redux, successfully optimizing client-facing dashboards to improve load times by 20%. On the backend, I designed and maintained microservices using Node.js and SQL databases. Although my primary backend experience is in Node.js, I am highly adaptable and have already begun building local projects with Ruby on Rails to ensure a rapid onboarding process into Shopify's ecosystem.

Working in Canada's tech corridor has shown me the immense value of bilingual collaboration. I am fully equipped to write clean technical documentation in English while engaging in daily standups, code reviews, and merchant communications in both French and English. 

Thank you for your time and consideration. I look forward to discussing how my technical background and bilingual capabilities align with Shopify's goals.

Sincerely,

Jean-Pierre Tremblay""",
        
        "checklist": [
            "Tailor resume resume headline and summary",
            "Refine achievement-based bullet points",
            "Draft tailored cover letter",
            "Verify French technical vocabulary and practice bilingual pitch transitions",
            "Proofread bilingual cover letter formatting",
            "Confirm educational credentials on resume",
            "Perform final proofreading of the application package"
        ]
    }
}

# --- MAIN APP LOGIC ---

st.write("# 🇨🇦 ApplyWise <span class='text-gradient'>AI</span>", unsafe_allow_html=True)
st.write("### Bilingual Career Agent for Canadian Tech Job Seekers (Kaggle Capstone Demo)")
st.write("---")

# Sidebar Configuration
st.sidebar.header("🛠️ Configuration")

# API Key and Mode
api_key = st.sidebar.text_input("Gemini API Key", type="password", help="Get a free key from Google AI Studio")
demo_mode = st.sidebar.toggle("Demo / Simulation Mode", value=True, help="Disable API calls and use pre-computed capstone outputs for a fast 5-minute demo")

# Model Selection
model_option = st.sidebar.selectbox(
    "Select Model",
    ["gemini-2.5-flash", "gemini-2.5-pro"],
    index=0
)

# Load Preset Template
st.sidebar.subheader("templates Preset Templates")
preset_option = st.sidebar.selectbox(
    "Load Example Job & Profile",
    ["None", "Shopify - Bilingual Developer", "Coveo - Senior DevOps Engineer"]
)

# Main Grid: Inputs
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Job Posting / Description")
    default_jd = ""
    if preset_option != "None":
        default_jd = PRESET_JOBS.get(preset_option, "")
    jd_text = st.text_area("Paste the job description here:", value=default_jd, height=300, placeholder="Include requirements, tech stack, and location...")

with col2:
    st.subheader("👤 Candidate Profile / Resume")
    default_resume = ""
    if preset_option != "None":
        default_resume = PRESET_CANDIDATES.get(preset_option, "")
    resume_text = st.text_area("Paste your profile or resume here:", value=default_resume, height=300, placeholder="Include skills, experience, and language proficiencies...")

# Trigger Button
run_clicked = st.button("🚀 Analyze & Generate Application Package", use_container_width=True)

# Main Output Area
if run_clicked:
    if not jd_text or not resume_text:
        st.error("Please provide both a Job Description and a Candidate Profile.")
    else:
        st.write("### ⚙️ Multi-Agent Workflow Execution")
        
        # 1. Validation (MCP Tool)
        st.info("🤖 **Root Orchestrator**: Initializing workflow. Validating inputs...")
        
        if demo_mode:
            # Simulated Run
            with st.status("Running Multi-Agent Pipeline (Simulation Mode)...", expanded=True) as status:
                st.write("1. 🛠️ **MCP Server**: Validating inputs...")
                st.write("2. 🔍 **Job Analyzer Agent**: Extracting metadata and keywords...")
                st.write("3. 📊 **Candidate Fit Agent**: Comparing profiles and calculating match score...")
                st.write("4. 📄 **Resume Tailor Agent**: Re-writing summary and formatting bullet points...")
                st.write("5. 💬 **Interview Coach Agent**: Preparing questions and bilingual pitches...")
                status.update(label="Workflow Complete!", state="complete")
                
            # Load simulated output
            sim_key = preset_option if preset_option in SIMULATED_OUTPUTS else "Shopify - Bilingual Developer"
            output = SIMULATED_OUTPUTS[sim_key]
            
            # Save to session state
            st.session_state["output"] = output
            
        else:
            # Live ADK Run
            if not api_key:
                st.error("Please provide a Gemini API Key in the sidebar to run in Live Mode, or enable Demo Mode.")
            else:
                st.info("Running live agents...")
                # Async runner execution
                try:
                    os.environ["GEMINI_MODEL"] = model_option
                    
                    # Define the async function to run the agent
                    async def execute_pipeline():
                        from agent import root_orchestrator
                        from google.adk.runners import InMemoryRunner
                        
                        runner = InMemoryRunner(agent=root_orchestrator, app_name="applywise_orchestrator")
                        session = await runner.session_service.create_session_async(
                            app_name="applywise_orchestrator",
                            user_id="capstone_user"
                        )
                        
                        session.state["job_description"] = jd_text
                        session.state["candidate_profile"] = resume_text
                        
                        os.environ["GEMINI_API_KEY"] = api_key
                        
                        async for event in runner.run_async(session=session):
                            pass
                            
                        updated_session = await runner.session_service.get_session_async(
                            app_name="applywise_orchestrator",
                            user_id="capstone_user",
                            session_id=session.id
                        )
                        return updated_session.state

                    # Run the async pipeline in Streamlit
                    with st.spinner("Executing Google ADK Agents & MCP Tools..."):
                        loop = asyncio.new_event_loop()
                        asyncio.set_event_loop(loop)
                        state = loop.run_until_complete(execute_pipeline())
                    
                    # Parse agent outputs
                    st.session_state["output"] = {
                        "job_analysis": state.get("job_analysis", "No job analysis generated."),
                        "candidate_fit": state.get("candidate_fit", "No fit analysis generated."),
                        "resume_tailoring": state.get("resume_tailoring", "No resume assets generated."),
                        "interview_coaching": state.get("interview_coaching", "No coaching assets generated."),
                        "cover_letter": state.get("resume_tailoring", ""), # Usually merged or separate
                        "checklist": ["Complete profile review", "Proofread cover letter"]
                    }
                    st.success("Analysis Complete!")
                except Exception as e:
                    st.error(f"Error during agent execution: {str(e)}")

# Display Outputs if available
if "output" in st.session_state:
    out = st.session_state["output"]
    
    st.write("---")
    st.write("## 🎁 Generated Application Package")
    
    # Define tabs matching the 12 required outputs
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "🔍 Job Analysis", 
        "📊 Candidate Fit", 
        "📄 Resume Tailor", 
        "✉️ Cover Letter", 
        "💬 Interview Prep & Pitch"
    ])
    
    with tab1:
        st.markdown(out.get("job_analysis", ""))
        
    with tab2:
        st.markdown(out.get("candidate_fit", ""))
        
    with tab3:
        st.markdown(out.get("resume_tailoring", ""))
        
    with tab4:
        st.subheader("✉️ Tailored Cover Letter")
        st.write("Click inside the card below to copy or edit the text.")
        st.markdown(f"<div class='paper-container'>{out.get('cover_letter', '')}</div>", unsafe_allow_html=True)
        
    with tab5:
        st.markdown(out.get("interview_coaching", ""))
        
    # Bottom: Checklist Section
    st.write("---")
    st.subheader("✅ Final Application Checklist")
    checklist_items = out.get("checklist", [])
    for idx, item in enumerate(checklist_items):
        st.checkbox(item, key=f"chk_{idx}")
