# ApplyWise AI - Multi-Agent Architecture

This document describes the multi-agent architecture and Model Context Protocol (MCP) design of **ApplyWise AI**.

---

## 🏗️ System Architecture

ApplyWise AI utilizes a **pipe-and-filter multi-agent pipeline** managed by a central orchestrator. The pipeline is implemented using **Google's Agent Development Kit (ADK)** and interacts with a **local MCP server** to execute deterministic text-processing and validation tasks.

```
+---------------------------------------------------------------------------------+
|                                STREAMLIT UI                                     |
|                      (Input: JD & Candidate Profile)                           |
+--------------------------------------+------------------------------------------+
                                       |
                                       v
+---------------------------------------------------------------------------------+
|                         ROOT ORCHESTRATOR AGENT                                 |
|                 (Chains sub-agents via SequentialAgent)                         |
+--------------------------------------+------------------------------------------+
                                       |
                                       +------(1)------> [Job Analyzer Agent]
                                       |
                                       +------(2)------> [Candidate Fit Agent]
                                       |
                                       +------(3)------> [Resume Tailor Agent]
                                       |
                                       +------(4)------> [Interview Coach Agent]
                                       |
                                       v
+---------------------------------------------------------------------------------+
|                               LOCAL MCP SERVER                                  |
|            (Exposes tools to agents via StdIn/StdOut Connection)                |
|                                                                                 |
|  [validate_inputs]        [extract_keywords]      [calculate_match_score]      |
|  [detect_missing_skills]  [format_resume_bullet]  [generate_checklist]         |
+---------------------------------------------------------------------------------+
```

---

## 🤖 Agent Definitions (Google ADK)

1. **Root Orchestrator Agent (`SequentialAgent`)**:
   - Manages the execution sequence.
   - Initial inputs (job description and candidate profile) are injected into the session state.
   - Sequentially invokes each specialized agent.
   - Collects and aggregates outputs in the session state for the Streamlit UI.

2. **Job Analyzer Agent (`LlmAgent`)**:
   - **Role**: Reads the job posting and extracts metadata (title, company, location, seniority, work mode), key responsibilities, and required/preferred skills.
   - **Tool Usage**: Calls the MCP `extract_keywords` tool to obtain a standardized, cleaned list of technical skills.
   - **Output Key**: `job_analysis`

3. **Candidate Fit Agent (`LlmAgent`)**:
   - **Role**: Compares the candidate's profile against the job analysis.
   - **Tool Usage**: Calls `extract_keywords` on the candidate profile, then calls `calculate_match_score` and `detect_missing_skills` to compare the two keyword lists.
   - **Output Key**: `candidate_fit`

4. **Resume Tailor Agent (`LlmAgent`)**:
   - **Role**: Generates a tailored resume headline, professional summary, and skills section.
   - **Tool Usage**: Rewrites candidate achievements into high-impact bullet points and calls `format_resume_bullet` to format them using the Google formula.
   - **Output Key**: `resume_tailoring`

5. **Interview Coach Agent (`LlmAgent`)**:
   - **Role**: Generates likely interview questions, STAR-based answers, technical prep notes, and a bilingual pitch.
   - **Tool Usage**: Analyzes the gaps identified by the Fit Agent to tailor behavioral and technical questions.
   - **Output Key**: `interview_coaching`

---

## 🛠️ Model Context Protocol (MCP) Tools

Exposing these utility functions as MCP tools allows the LLM-based agents to perform deterministic calculations (like matching arrays or formatting strings) instead of hallucinating math or syntax.

- **`validate_inputs(jd, resume)`**: Ensures inputs are non-empty and meet minimum length.
- **`extract_keywords(text)`**: Scans text against a dictionary of 60+ common Canadian tech keywords.
- **`calculate_match_score(jd_keywords, resume_keywords)`**: Computes the percentage of overlap between required skills and candidate skills.
- **`detect_missing_skills(jd_keywords, resume_keywords)`**: Computes the set difference of required skills minus candidate skills.
- **`format_resume_bullet(bullet, action_verb, result)`**: Formats achievements using the Google formula.
- **`generate_checklist(jd_text)`**: Creates a list of tasks (e.g. bilingual checks, portfolio updates) based on JD triggers.
