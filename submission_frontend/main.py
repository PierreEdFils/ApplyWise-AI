import os
import uuid
from datetime import datetime, timezone
from typing import Any, List, Optional
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(
    title="ApplyWise AI — Career Review Dashboard",
    version="0.1.0",
)

# --- Pydantic Schemas ---
class ActionRequest(BaseModel):
    approved: bool
    reviewer_note: str = ""

class FinalReview(BaseModel):
    id: str
    timestamp: str
    candidate: str
    job_title: str
    company: str
    decision: str
    reviewer_note: str
    match_score: int
    summary: str
    next_steps: List[str]

class ActionResponse(BaseModel):
    session_id: str
    decision: str
    reviewer_note: str
    final_review: FinalReview

# --- Mock In-Memory Data ---
MOCK_PENDING_REVIEWS = [
    {
        "session_id": "session_ca_tech_001",
        "interrupt_id": "interrupt_wait_review_01",
        "candidate_name": "Pierre Ed Fils",
        "job_title": "Senior Fullstack Developer (Bilingual English/French)",
        "company": "ApplyWise AI",
        "match_score": 92,
        "top_skills": [
            "Python (FastAPI, Django)",
            "React / TypeScript",
            "Google Cloud Platform (GCP)",
            "Microservices (GKE, Cloud Run)",
            "Bilingual English/French"
        ],
        "missing_skills": [
            "Explicit passion/projects in AI (implied, needs highlighting)",
            "Direct Flask experience (covered by FastAPI/Django)"
        ],
        "resume_headline": "Senior Fullstack Software Engineer | Python, React, TypeScript, GCP | Bilingual (EN/FR)",
        "application_package": {
            "job_summary": "ApplyWise AI is seeking a Senior Fullstack Developer (Bilingual English/French) for a hybrid role in Ottawa, ON. The primary responsibility involves building next-gen developer tools using Python, React, TypeScript, and GCP.",
            "professional_summary": "English: Highly accomplished Senior Fullstack Software Engineer with 5 years of experience building scalable web applications. Proven leader in designing and implementing microservices on GCP, eager to leverage bilingual proficiency and a passion for innovation to build next-generation developer tools at ApplyWise AI.\n\nFrench: Ingénieur Logiciel Fullstack Senior hautement accompli avec 5 ans d'expérience dans la création d'applications web évolutives. Leader avéré dans la conception et l'implémentation de microservices sur GCP, désireux de mettre à profit sa maîtrise bilingue et sa passion pour l'innovation pour développer des outils de nouvelle génération chez ApplyWise AI.",
            "resume_bullet_points": [
                "English: Led a team of 3 developers in the successful migration of a critical legacy system to modern architecture, resulting in a 40% performance improvement.\nFrench: Dirigé une équipe de 3 développeurs dans la migration réussie d'un système hérité critique vers une architecture moderne, entraînant une amélioration de 40% des performances.",
                "English: Designed and implemented scalable microservices architecture on GCP using GKE and Cloud Run, ensuring high availability.\nFrench: Conçu et implémenté une architecture de microservices évolutive sur GCP à l'aide de GKE et Cloud Run, assurant une haute disponibilité."
            ],
            "cover_letter_draft": "Dear Hiring Manager,\n\nI am writing to express my strong interest in the Senior Fullstack Developer position at ApplyWise AI. With my 5 years of experience in fullstack web development, coupled with my proficiency in Python (FastAPI, Django), React, TypeScript, and Google Cloud Platform (GCP), I am confident I possess the technical skills and leadership qualities to excel in this role.\n\nSincerely,\nPierre Ed Fils",
            "interview_questions": [
                "Question: Tell me about a time you led a complex technical migration. Guidance: Focus on the 40% performance improvement and GKE/Cloud Run choices.",
                "Question: How do you approach building next-gen developer tools? Guidance: Elaborate on API design, performance optimization, and developer experience."
            ],
            "bilingual_pitch": "English: Hello! I'm Pierre Ed Fils, a Senior Fullstack Software Engineer. My expertise in Python, React, TypeScript, and GCP, combined with bilingual fluency, makes me an ideal fit to build next-gen developer tools at ApplyWise AI.\n\nFrench: Bonjour ! Je suis Pierre Ed Fils, ingénieur logiciel Fullstack Senior. Mon expertise en Python, React, TypeScript et GCP, combinée à ma maîtrise parfaite de l'anglais et du français, fait de moi un candidat idéal pour créer les outils développeurs de nouvelle génération chez ApplyWise AI.",
            "application_checklist": [
                "Tailor resume and cover letter to explicitly highlight interest in AI.",
                "Prepare specific examples demonstrating excellent communication and leadership.",
                "Practice discussing technical concepts in both English and French."
            ]
        }
    },
    {
        "session_id": "session_ca_tech_002",
        "interrupt_id": "interrupt_wait_review_02",
        "candidate_name": "Sarah Jenkins",
        "job_title": "Cloud DevOps Engineer",
        "company": "Northern Cloud Solutions",
        "match_score": 85,
        "top_skills": [
            "Terraform / Infrastructure as Code",
            "CI/CD (GitHub Actions, GitLab CI)",
            "AWS (EKS, ECS, Lambda)",
            "Docker / Kubernetes",
            "Python scripting"
        ],
        "missing_skills": [
            "Bilingualism (English/French) is preferred but candidate is English-only",
            "Azure or GCP experience (job prefers multi-cloud)"
        ],
        "resume_headline": "Cloud DevOps & Infrastructure Engineer | Terraform, Kubernetes, AWS, CI/CD",
        "application_package": {
            "job_summary": "Northern Cloud Solutions is looking for a Cloud DevOps Engineer in Toronto, ON (Remote-first). The role focuses on automating infrastructure provisioning, managing Kubernetes clusters, and maintaining secure CI/CD pipelines.",
            "professional_summary": "Dedicated Cloud DevOps Engineer with 4 years of experience specializing in automating cloud infrastructure and orchestrating containerized environments. Expert in Terraform and Kubernetes, with a proven track record of reducing deployment times by 35%.",
            "resume_bullet_points": [
                "Architected and maintained multi-region Kubernetes clusters on AWS (EKS), improving infrastructure reliability to 99.99% uptime.",
                "Designed and implemented automated CI/CD pipelines using GitHub Actions, reducing deployment cycle times from days to minutes."
            ],
            "cover_letter_draft": "Dear Northern Cloud Solutions Team,\n\nI am thrilled to apply for the Cloud DevOps Engineer position. My background in automating infrastructure with Terraform and managing containerized deployments with Kubernetes aligns perfectly with your scaling goals.\n\nSincerely,\nSarah Jenkins",
            "interview_questions": [
                "Question: Explain your approach to managing state in Terraform across large teams. Guidance: Highlight remote state locks, modular design, and workspace strategy.",
                "Question: How do you secure Kubernetes workloads in public cloud environments? Guidance: Discuss network policies, IAM roles for service accounts, and secrets management."
            ],
            "bilingual_pitch": "English: I'm Sarah Jenkins, a DevOps Engineer passionate about automation, reliability, and cloud architecture. I specialize in Terraform and Kubernetes and look forward to scaling your infrastructure.",
            "application_checklist": [
                "Highlight multi-cloud interest and willingness to learn GCP/Azure.",
                "Prepare case studies on disaster recovery and infrastructure scaling."
            ]
        }
    }
]

ACTIONED_REVIEWS = {}

# --- API Endpoints ---
@app.get("/api/pending", response_model=List[dict])
def get_pending_reviews():
    """Returns the list of pending application packages awaiting review."""
    pending = [
        review for review in MOCK_PENDING_REVIEWS
        if review["session_id"] not in ACTIONED_REVIEWS
    ]
    return pending

@app.post("/api/action/{session_id}", response_model=ActionResponse)
def submit_action(session_id: str, request: ActionRequest):
    """Submits the reviewer's approval or rejection, returning a final career review."""
    review_data = next(
        (r for r in MOCK_PENDING_REVIEWS if r["session_id"] == session_id), None
    )
    if not review_data:
        raise HTTPException(status_code=404, detail="Session not found")
        
    decision = "Approved" if request.approved else "Rejected"
    
    final_review = FinalReview(
        id=f"rev_{uuid.uuid4().hex[:8]}",
        timestamp=datetime.now(timezone.utc).isoformat(),
        candidate=review_data["candidate_name"],
        job_title=review_data["job_title"],
        company=review_data["company"],
        decision=decision,
        reviewer_note=request.reviewer_note or "No additional notes provided.",
        match_score=review_data["match_score"],
        summary=f"The application package for {review_data['candidate_name']} applying to {review_data['company']} has been reviewed and {decision.lower()}.",
        next_steps=[
            "Export the tailored resume and cover letter.",
            "Begin mock interview prep with the generated questions.",
            "Review the bilingual pitch and practice delivery."
        ] if request.approved else [
            "Re-evaluate the candidate profile against job requirements.",
            "Update missing skills and re-run the tailoring assistant."
        ]
    )
    
    response = ActionResponse(
        session_id=session_id,
        decision=decision,
        reviewer_note=request.reviewer_note,
        final_review=final_review
    )
    
    ACTIONED_REVIEWS[session_id] = response
    return response

# --- Dashboard UI HTML ---
DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ApplyWise AI — Career Review Dashboard</title>
    <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&family=Plus+Jakarta+Sans:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0b0f19;
            --card-bg: rgba(255, 255, 255, 0.03);
            --card-border: rgba(255, 255, 255, 0.08);
            --text-primary: #f8fafc;
            --text-secondary: #94a3b8;
            --accent-primary: #8b5cf6;
            --accent-secondary: #ec4899;
            --accent-green: #10b981;
            --accent-red: #ef4444;
            --glass-blur: blur(20px);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-primary);
            min-height: 100vh;
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(139, 92, 246, 0.15) 0%, transparent 40%),
                radial-gradient(circle at 90% 80%, rgba(236, 72, 153, 0.12) 0%, transparent 40%);
            background-attachment: fixed;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2.5rem 1.5rem;
        }

        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 3rem;
            border-bottom: 1px solid var(--card-border);
            padding-bottom: 1.5rem;
        }

        h1 {
            font-family: 'Outfit', sans-serif;
            font-size: 2.25rem;
            font-weight: 700;
            background: linear-gradient(to right, #a78bfa, #f472b6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .subtitle {
            color: var(--text-secondary);
            font-size: 0.95rem;
            margin-top: 0.25rem;
        }

        .stats-badge {
            background: rgba(139, 92, 246, 0.15);
            border: 1px solid rgba(139, 92, 246, 0.3);
            padding: 0.5rem 1rem;
            border-radius: 9999px;
            font-size: 0.85rem;
            font-weight: 600;
            color: #c084fc;
        }

        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 2rem;
        }

        .card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 1.25rem;
            padding: 1.75rem;
            backdrop-filter: var(--glass-blur);
            -webkit-backdrop-filter: var(--glass-blur);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: linear-gradient(to right, var(--accent-primary), var(--accent-secondary));
            opacity: 0;
            transition: opacity 0.3s ease;
        }

        .card:hover {
            transform: translateY(-5px);
            border-color: rgba(255, 255, 255, 0.15);
            box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4);
        }

        .card:hover::before {
            opacity: 1;
        }

        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            margin-bottom: 1.25rem;
        }

        .candidate-name {
            font-family: 'Outfit', sans-serif;
            font-size: 1.35rem;
            font-weight: 600;
            margin-bottom: 0.25rem;
        }

        .job-title {
            font-size: 0.9rem;
            color: var(--text-secondary);
            font-weight: 500;
        }

        .company-name {
            font-size: 0.85rem;
            color: #a78bfa;
            margin-top: 0.15rem;
            font-weight: 600;
        }

        .match-badge {
            width: 50px;
            height: 50px;
            border-radius: 50px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Outfit', sans-serif;
            font-weight: 700;
            font-size: 1.1rem;
            background: linear-gradient(135deg, rgba(139, 92, 246, 0.2) 0%, rgba(236, 72, 153, 0.2) 100%);
            border: 2px solid var(--accent-primary);
        }

        .skills-list {
            margin: 1.25rem 0;
        }

        .skills-title {
            font-size: 0.75rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            color: var(--text-secondary);
            margin-bottom: 0.5rem;
            font-weight: 700;
        }

        .tags-container {
            display: flex;
            flex-wrap: wrap;
            gap: 0.4rem;
        }

        .tag {
            font-size: 0.75rem;
            padding: 0.25rem 0.6rem;
            border-radius: 0.375rem;
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        .tag.matching {
            background: rgba(16, 185, 129, 0.1);
            border-color: rgba(16, 185, 129, 0.2);
            color: #34d399;
        }

        .tag.missing {
            background: rgba(239, 68, 68, 0.1);
            border-color: rgba(239, 68, 68, 0.2);
            color: #f87171;
        }

        .card-actions {
            display: flex;
            gap: 0.75rem;
            margin-top: 1.5rem;
        }

        button {
            font-family: 'Plus Jakarta Sans', sans-serif;
            font-weight: 600;
            font-size: 0.85rem;
            padding: 0.625rem 1rem;
            border-radius: 0.5rem;
            border: none;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 0.5rem;
        }

        .btn-view {
            background: rgba(255, 255, 255, 0.08);
            color: var(--text-primary);
            flex-grow: 1;
            border: 1px solid rgba(255, 255, 255, 0.05);
        }

        .btn-view:hover {
            background: rgba(255, 255, 255, 0.15);
        }

        .btn-approve {
            background: var(--accent-green);
            color: #ffffff;
        }

        .btn-approve:hover {
            background: #059669;
            box-shadow: 0 4px 12px rgba(16, 185, 129, 0.3);
        }

        .btn-reject {
            background: var(--accent-red);
            color: #ffffff;
        }

        .btn-reject:hover {
            background: #dc2626;
            box-shadow: 0 4px 12px rgba(239, 68, 68, 0.3);
        }

        /* --- Slide-out Modal --- */
        .modal-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.6);
            backdrop-filter: blur(5px);
            z-index: 100;
            opacity: 0;
            pointer-events: none;
            transition: opacity 0.3s ease;
        }

        .modal-overlay.active {
            opacity: 1;
            pointer-events: auto;
        }

        .modal {
            position: fixed;
            top: 0;
            right: -600px;
            width: 100%;
            max-width: 580px;
            height: 100%;
            background: #0e1321;
            border-left: 1px solid var(--card-border);
            z-index: 101;
            padding: 2.5rem;
            overflow-y: auto;
            transition: right 0.35s cubic-bezier(0.4, 0, 0.2, 1);
            box-shadow: -10px 0 30px rgba(0, 0, 0, 0.5);
        }

        .modal.active {
            right: 0;
        }

        .modal-close {
            position: absolute;
            top: 1.5rem;
            right: 1.5rem;
            background: transparent;
            color: var(--text-secondary);
            font-size: 1.5rem;
            cursor: pointer;
            border: none;
        }

        .modal-close:hover {
            color: var(--text-primary);
        }

        .modal-section {
            margin-bottom: 2rem;
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.04);
            border-radius: 0.75rem;
            padding: 1.25rem;
        }

        .modal-section-title {
            font-family: 'Outfit', sans-serif;
            font-size: 1.05rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
            color: #c084fc;
            border-bottom: 1px solid rgba(255, 255, 255, 0.05);
            padding-bottom: 0.5rem;
        }

        .scrollable-content {
            max-height: 200px;
            overflow-y: auto;
            background: rgba(0, 0, 0, 0.2);
            padding: 0.75rem;
            border-radius: 0.5rem;
            font-size: 0.85rem;
            line-height: 1.5;
            white-space: pre-wrap;
        }

        .modal-action-bar {
            position: sticky;
            bottom: 0;
            background: #0e1321;
            padding-top: 1rem;
            border-top: 1px solid rgba(255, 255, 255, 0.05);
            display: flex;
            flex-direction: column;
            gap: 1rem;
        }

        .notes-textarea {
            width: 100%;
            height: 70px;
            background: rgba(255, 255, 255, 0.04);
            border: 1px solid var(--card-border);
            border-radius: 0.5rem;
            color: var(--text-primary);
            padding: 0.75rem;
            font-family: inherit;
            resize: none;
            outline: none;
        }

        .notes-textarea:focus {
            border-color: var(--accent-primary);
        }

        .modal-buttons {
            display: flex;
            gap: 1rem;
        }

        /* --- Loading Spinner --- */
        .spinner {
            width: 16px;
            height: 16px;
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-top-color: #fff;
            border-radius: 50%;
            animation: spin 0.8s infinite linear;
            display: none;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        .loading .spinner {
            display: block;
        }
        
        .loading span {
            display: none;
        }

        /* --- Empty State --- */
        .empty-state {
            grid-column: 1 / -1;
            text-align: center;
            padding: 5rem 2rem;
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 1.25rem;
            color: var(--text-secondary);
        }

        .empty-state h3 {
            font-family: 'Outfit', sans-serif;
            color: var(--text-primary);
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }

        /* --- Result Notification --- */
        .result-panel {
            margin-top: 1.5rem;
            padding: 1rem;
            border-radius: 0.75rem;
            font-size: 0.85rem;
            display: none;
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .result-panel.approved {
            background: rgba(16, 185, 129, 0.1);
            border: 1px solid rgba(16, 185, 129, 0.2);
            color: #34d399;
        }

        .result-panel.rejected {
            background: rgba(239, 68, 68, 0.1);
            border: 1px solid rgba(239, 68, 68, 0.2);
            color: #f87171;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <div>
                <h1>ApplyWise AI</h1>
                <div class="subtitle">Bilingual Tech Career Application Review Hub</div>
            </div>
            <div class="stats-badge">
                <span id="pending-count">0</span> Pending Reviews
            </div>
        </header>

        <div class="grid" id="reviews-grid">
            <!-- Rendered dynamically -->
        </div>
    </div>

    <!-- Slide-out Modal -->
    <div class="modal-overlay" id="modal-overlay" onclick="closeModal()"></div>
    <div class="modal" id="review-modal">
        <button class="modal-close" onclick="closeModal()">&times;</button>
        <h2 id="modal-candidate-name" style="font-family: 'Outfit', sans-serif; font-size: 1.75rem; margin-bottom: 0.25rem;"></h2>
        <div id="modal-job-title" style="color: var(--accent-primary); font-weight: 600; margin-bottom: 1.5rem;"></div>

        <div class="modal-section">
            <div class="modal-section-title">Job Summary</div>
            <div id="modal-job-summary" style="font-size: 0.9rem; line-height: 1.6;"></div>
        </div>

        <div class="modal-section">
            <div class="modal-section-title">Tailored Professional Summary</div>
            <div id="modal-professional-summary" class="scrollable-content"></div>
        </div>

        <div class="modal-section">
            <div class="modal-section-title">Bilingual Elevator Pitch</div>
            <div id="modal-bilingual-pitch" class="scrollable-content"></div>
        </div>

        <div class="modal-section">
            <div class="modal-section-title">Tailored Cover Letter Draft</div>
            <div id="modal-cover-letter" class="scrollable-content"></div>
        </div>

        <div class="modal-section">
            <div class="modal-section-title">Tailored Resume Bullet Points</div>
            <div id="modal-bullets" class="scrollable-content"></div>
        </div>

        <div class="modal-section">
            <div class="modal-section-title">Bilingual Interview Questions</div>
            <div id="modal-questions" class="scrollable-content"></div>
        </div>

        <div class="modal-section">
            <div class="modal-section-title">Application Checklist</div>
            <div id="modal-checklist" class="scrollable-content"></div>
        </div>

        <div class="modal-action-bar">
            <div>
                <label for="reviewer-notes" style="font-size: 0.8rem; font-weight: 600; color: var(--text-secondary); display: block; margin-bottom: 0.35rem;">Reviewer Notes (Optional)</label>
                <textarea id="reviewer-notes" class="notes-textarea" placeholder="Add comments, recommended changes, or feedback..."></textarea>
            </div>
            <div class="modal-buttons">
                <button class="btn-approve" onclick="submitReview(true)" style="flex: 1; padding: 0.85rem;">
                    <div class="spinner"></div>
                    <span>✓ Approve Package</span>
                </button>
                <button class="btn-reject" onclick="submitReview(false)" style="flex: 1; padding: 0.85rem;">
                    <div class="spinner"></div>
                    <span>✗ Reject Package</span>
                </button>
            </div>
            <div id="modal-result-panel" class="result-panel"></div>
        </div>
    </div>

    <script>
        let pendingReviews = [];
        let activeSessionId = null;

        async function fetchPending() {
            try {
                const response = await fetch('/api/pending');
                pendingReviews = await response.json();
                document.getElementById('pending-count').textContent = pendingReviews.length;
                renderDashboard();
            } catch (error) {
                console.error("Error fetching pending reviews:", error);
            }
        }

        function renderDashboard() {
            const grid = document.getElementById('reviews-grid');
            grid.innerHTML = '';

            if (pendingReviews.length === 0) {
                grid.innerHTML = `
                    <div class="empty-state">
                        <h3>All caught up!</h3>
                        <p>There are no pending career application packages awaiting review.</p>
                    </div>
                `;
                return;
            }

            pendingReviews.forEach(review => {
                const card = document.createElement('div');
                card.className = 'card';
                card.innerHTML = `
                    <div>
                        <div class="card-header">
                            <div>
                                <div class="candidate-name">${review.candidate_name}</div>
                                <div class="job-title">${review.job_title}</div>
                                <div class="company-name">${review.company}</div>
                            </div>
                            <div class="match-badge">${review.match_score}%</div>
                        </div>

                        <div class="skills-list">
                            <div class="skills-title">Matching Strengths</div>
                            <div class="tags-container">
                                ${review.top_skills.slice(0, 3).map(skill => `<span class="tag matching">${skill}</span>`).join('')}
                            </div>
                        </div>

                        <div class="skills-list">
                            <div class="skills-title">Key Missing Skills</div>
                            <div class="tags-container">
                                ${review.missing_skills.slice(0, 2).map(skill => `<span class="tag missing">${skill}</span>`).join('')}
                            </div>
                        </div>
                    </div>

                    <div>
                        <div style="font-size: 0.8rem; color: var(--text-secondary); margin-bottom: 0.25rem; font-weight: 600;">Resume Headline</div>
                        <div style="font-size: 0.85rem; font-style: italic; color: var(--text-primary); line-height: 1.4; background: rgba(255,255,255,0.02); padding: 0.5rem; border-radius: 0.375rem; border: 1px solid rgba(255,255,255,0.03);">
                            "${review.resume_headline}"
                        </div>
                        <div class="card-actions">
                            <button class="btn-view" onclick="openModal('${review.session_id}')">View Details</button>
                            <button class="btn-approve" id="quick-approve-${review.session_id}" onclick="quickAction('${review.session_id}', true)">
                                <div class="spinner"></div>
                                <span>Approve</span>
                            </button>
                        </div>
                    </div>
                `;
                grid.appendChild(card);
            });
        }

        function openModal(sessionId) {
            const review = pendingReviews.find(r => r.session_id === sessionId);
            if (!review) return;

            activeSessionId = sessionId;
            document.getElementById('modal-candidate-name').textContent = review.candidate_name;
            document.getElementById('modal-job-title').textContent = `${review.job_title} @ ${review.company}`;
            document.getElementById('modal-job-summary').textContent = review.application_package.job_summary;
            document.getElementById('modal-professional-summary').textContent = review.application_package.professional_summary;
            document.getElementById('modal-bilingual-pitch').textContent = review.application_package.bilingual_pitch;
            document.getElementById('modal-cover-letter').textContent = review.application_package.cover_letter_draft;
            
            // Format list arrays into text blocks
            document.getElementById('modal-bullets').textContent = review.application_package.resume_bullet_points.join('\\n\\n');
            document.getElementById('modal-questions').textContent = review.application_package.interview_questions.join('\\n\\n');
            document.getElementById('modal-checklist').textContent = review.application_package.application_checklist.map(item => `• ${item}`).join('\\n');

            document.getElementById('reviewer-notes').value = '';
            document.getElementById('modal-result-panel').style.display = 'none';

            document.getElementById('modal-overlay').classList.add('active');
            document.getElementById('review-modal').classList.add('active');
        }

        function closeModal() {
            document.getElementById('modal-overlay').classList.remove('active');
            document.getElementById('review-modal').classList.remove('active');
            activeSessionId = null;
        }

        async function quickAction(sessionId, approved) {
            const btn = document.getElementById(`quick-approve-${sessionId}`);
            btn.classList.add('loading');
            
            try {
                const response = await fetch(`/api/action/${sessionId}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ approved, reviewer_note: "Approved via quick action." })
                });
                
                if (response.ok) {
                    setTimeout(() => {
                        btn.classList.remove('loading');
                        fetchPending();
                    }, 800);
                }
            } catch (error) {
                console.error("Error executing quick action:", error);
                btn.classList.remove('loading');
            }
        }

        async function submitReview(approved) {
            if (!activeSessionId) return;

            const note = document.getElementById('reviewer-notes').value;
            const buttons = document.querySelectorAll('.modal-buttons button');
            const clickedBtn = approved ? buttons[0] : buttons[1];
            
            clickedBtn.classList.add('loading');
            buttons.forEach(b => b.disabled = true);

            try {
                const response = await fetch(`/api/action/${activeSessionId}`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ approved, reviewer_note: note })
                });

                if (response.ok) {
                    const data = await response.json();
                    const resultPanel = document.getElementById('modal-result-panel');
                    resultPanel.className = `result-panel ${approved ? 'approved' : 'rejected'}`;
                    resultPanel.innerHTML = `
                        <strong>Package ${approved ? 'Approved' : 'Rejected'}!</strong><br>
                        Decision logged. Final review ID: <code>${data.final_review.id}</code><br>
                        <em>Closing panel...</em>
                    `;
                    resultPanel.style.display = 'block';

                    setTimeout(() => {
                        clickedBtn.classList.remove('loading');
                        buttons.forEach(b => b.disabled = false);
                        closeModal();
                        fetchPending();
                    }, 2000);
                }
            } catch (error) {
                console.error("Error submitting review:", error);
                clickedBtn.classList.remove('loading');
                buttons.forEach(b => b.disabled = false);
            }
        }

        // Initialize dashboard
        fetchPending();
    </script>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def get_dashboard():
    """Renders the dark glassmorphism review dashboard."""
    return DASHBOARD_HTML

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8501, reload=True)
