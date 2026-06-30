# ApplyWise AI 🇨🇦
### Bilingual Career Agent for Canadian Tech Job Seekers

ApplyWise AI is a Python-based **multi-agent system** designed to help bilingual tech job seekers in Canada turn any job description and candidate profile into a complete, tailored application package. 

It is built using **Google's Agent Development Kit (ADK)** for agent orchestration, a **local Model Context Protocol (MCP) server** for deterministic utility tools, and **Streamlit** for a premium, interactive dashboard.

---

## 🌟 Key Features (12 Required Outputs)

1. **Job Summary**: Synthesized overview of the target role.
2. **Key Required Skills**: Highlighted tech stack and language needs.
3. **Match Score**: Calculated overlap score (0-100) using local MCP tools.
4. **Strong Matching Experience**: Candidate strengths matching the job description.
5. **Missing Skills or Gaps**: Gaps in the candidate's profile.
6. **Tailored Resume Headline**: ATS-optimized headline.
7. **Professional Resume Summary**: Hook for Canadian recruiters.
8. **Resume Bullet Points**: Achievement-oriented bullets formatted using the Google formula.
9. **Cover Letter Draft**: Custom-tailored cover letter in English or French.
10. **Interview Questions**: Likely behavioral and technical questions with STAR outlines.
11. **Bilingual Elevator Pitches**: 30-second pitches in both English and French.
12. **Final Application Checklist**: Action items based on job requirements.

---

## 🏗️ Multi-Agent Architecture

ApplyWise AI utilizes a pipeline of specialized agents coordinated by a **Root Orchestrator**:

- **Root Orchestrator (`SequentialAgent`)**: Controls the workflow and aggregates outputs in the session state.
- **Job Analyzer Agent (`LlmAgent`)**: Extracts job metadata and required skills.
- **Candidate Fit Agent (`LlmAgent`)**: Evaluates candidate fit, strengths, and gaps.
- **Resume Tailor Agent (`LlmAgent`)**: Tailors resume headline, summary, and bullet points.
- **Interview Coach Agent (`LlmAgent`)**: Generates interview questions, STAR outlines, and bilingual pitches.

All agents have access to a **local MCP server** (`mcp_server.py`) which exposes utility tools:
- `validate_inputs`: Validates character lengths and presence of inputs.
- `extract_keywords`: Scans text against a dictionary of common tech terms.
- `calculate_match_score`: Calculates the overlap percentage.
- `detect_missing_skills`: Identifies required skills missing from the resume.
- `format_resume_bullet`: Formats achievements using the Google formula.
- `generate_checklist`: Creates a checklist based on job requirements.

---

## 🚀 Getting Started

### 📦 Installation

1. Create a virtual environment and install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Copy the `.env.example` file to `.env` and configure your API key (optional if using Demo Mode):
   ```bash
   cp .env.example .env
   ```

### 💻 Running the App

Run the Streamlit application:
```bash
streamlit run app.py
```

Open your browser and navigate to `http://localhost:8501`.

---

## 🎪 5-Minute Capstone Demo Mode

To support a seamless 5-minute presentation or Kaggle capstone demo without waiting for LLM API latency:

1. Enable **Demo / Simulation Mode** in the Streamlit sidebar (enabled by default).
2. Select a preset template from the dropdown (e.g., **Shopify - Bilingual Developer**).
3. Click **Analyze & Generate Application Package**.
4. The dashboard will instantly populate all 12 outputs across organized, visual tabs.
5. To test live AI generation, toggle **Demo Mode** off, enter your **Gemini API Key** in the sidebar, and click analyze.
