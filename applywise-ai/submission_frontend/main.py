"""ApplyWise AI — Career Review Dashboard (Local Demo).

A FastAPI server that serves a dark glassmorphism dashboard for reviewing
pending application packages produced by the ApplyWise AI multi-agent
workflow.  This version uses **mock data** so it runs without Agent Runtime.

Endpoints
---------
GET  /             → HTML dashboard
GET  /api/pending  → JSON list of pending reviews
POST /api/action/{session_id}  → approve / reject a review
"""

from __future__ import annotations

import uuid
from datetime import datetime, timezone
from typing import Any

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# ---------------------------------------------------------------------------
# App
# ---------------------------------------------------------------------------

app = FastAPI(
    title="ApplyWise AI — Career Review Dashboard",
    version="0.1.0",
)

# ---------------------------------------------------------------------------
# Pydantic models
# ---------------------------------------------------------------------------


class ActionRequest(BaseModel):
    approved: bool
    reviewer_note: str = ""


class ActionResponse(BaseModel):
    session_id: str
    decision: str
    reviewer_note: str
    final_review: dict[str, Any]


# ---------------------------------------------------------------------------
# Mock data store  (replace with ADK session queries later)
# ---------------------------------------------------------------------------

MOCK_PACKAGES: list[dict[str, Any]] = [
    {
        "session_id": "sess-a1b2c3",
        "interrupt_id": "int-001",
        "created_at": "2026-06-30T02:15:00Z",
        "candidate_name": "Pierre Ed Fils",
        "job_title": "Senior Fullstack Developer (Bilingual EN/FR)",
        "company": "ApplyWise AI",
        "location": "Ottawa, ON — Hybrid",
        "match_score": 92,
        "top_skills": [
            "Python (FastAPI, Django)",
            "React / TypeScript",
            "Google Cloud Platform",
            "Microservices (GKE, Cloud Run)",
            "Bilingual EN/FR",
        ],
        "missing_skills": [
            "Flask experience",
            "Explicit AI / ML projects",
            "Ottawa relocation clarity",
        ],
        "resume_headline": (
            "Senior Fullstack Engineer · Python · React · GCP · Bilingual EN/FR"
        ),
        "professional_summary": (
            "Accomplished Senior Fullstack Engineer with 5 years of experience "
            "building scalable web applications in Python, React, and TypeScript. "
            "Proven leader on GCP (GKE & Cloud Run) who improved system performance "
            "by 40%. Bilingual English/French, ready to contribute in Ottawa."
        ),
        "cover_letter_draft": (
            "Dear Hiring Manager,\n\n"
            "I am writing to express my strong interest in the Senior Fullstack "
            "Developer position at ApplyWise AI. With 5 years of hands-on experience "
            "in Python (FastAPI, Django), React/TypeScript, and Google Cloud Platform, "
            "I bring the technical depth and leadership your team needs to build "
            "next-gen developer tools.\n\n"
            "At TechCorp I led a 3-person team that migrated a legacy monolith to "
            "microservices on GKE and Cloud Run, delivering a 40% performance gain. "
            "As a bilingual professional based in Montreal, I am eager to collaborate "
            "with your teams across Quebec and Ontario.\n\n"
            "Cordialement / Sincerely,\nPierre Ed Fils"
        ),
        "interview_questions": [
            "Describe a time you led a complex migration. What challenges did you face?",
            "How would you design a scalable API for a developer-tools platform?",
            "Tell me about collaborating across bilingual teams.",
        ],
        "bilingual_pitch": (
            "EN: Hi, I'm Pierre — a Senior Fullstack Engineer with 5 years in "
            "Python, React & GCP. I led a team that boosted performance 40% and "
            "I'm bilingual EN/FR.\n\n"
            "FR: Bonjour, je suis Pierre — ingénieur Fullstack Senior avec 5 ans "
            "d'expérience en Python, React et GCP. J'ai dirigé une équipe qui a "
            "amélioré les performances de 40% et je suis bilingue."
        ),
        "application_checklist": [
            "Tailor resume headline and summary",
            "Highlight AI interest in cover letter",
            "Prepare STAR answers for leadership questions",
            "Practice bilingual elevator pitch",
            "Confirm Ottawa relocation readiness",
        ],
    },
    {
        "session_id": "sess-d4e5f6",
        "interrupt_id": "int-002",
        "created_at": "2026-06-30T03:42:00Z",
        "candidate_name": "Marie-Claire Dupont",
        "job_title": "Cloud Data Engineer",
        "company": "Shopify",
        "location": "Toronto, ON — Remote",
        "match_score": 78,
        "top_skills": [
            "Python",
            "BigQuery",
            "Apache Beam / Dataflow",
            "SQL",
            "Terraform",
        ],
        "missing_skills": [
            "Spark / PySpark",
            "Kubernetes experience",
            "CI/CD pipeline ownership",
        ],
        "resume_headline": "Cloud Data Engineer · Python · BigQuery · Dataflow · Terraform",
        "professional_summary": (
            "Data Engineer with 3 years building ETL pipelines on GCP. "
            "Proficient in BigQuery, Dataflow, and Terraform. "
            "Seeking remote-first opportunities in Toronto."
        ),
        "cover_letter_draft": (
            "Dear Shopify Hiring Team,\n\n"
            "I am excited to apply for the Cloud Data Engineer role. "
            "My experience with BigQuery and Dataflow aligns well with "
            "Shopify's data platform needs.\n\n"
            "Best regards,\nMarie-Claire Dupont"
        ),
        "interview_questions": [
            "Walk me through an ETL pipeline you designed end-to-end.",
            "How do you handle schema evolution in BigQuery?",
            "Describe a data quality issue you caught and resolved.",
        ],
        "bilingual_pitch": (
            "EN: I'm Marie-Claire, a Cloud Data Engineer specializing in "
            "BigQuery, Dataflow, and Terraform on GCP.\n\n"
            "FR: Je suis Marie-Claire, ingénieure de données Cloud "
            "spécialisée en BigQuery, Dataflow et Terraform sur GCP."
        ),
        "application_checklist": [
            "Add Spark projects or certifications",
            "Emphasize Terraform automation wins",
            "Prepare pipeline design whiteboard answers",
            "Research Shopify's data stack",
        ],
    },
    {
        "session_id": "sess-g7h8i9",
        "interrupt_id": "int-003",
        "created_at": "2026-06-30T04:10:00Z",
        "candidate_name": "Amit Patel",
        "job_title": "ML Engineer — NLP",
        "company": "Cohere",
        "location": "Toronto, ON — Hybrid",
        "match_score": 85,
        "top_skills": [
            "PyTorch",
            "Transformers / HuggingFace",
            "Python",
            "Docker",
            "AWS SageMaker",
        ],
        "missing_skills": [
            "Production LLM fine-tuning at scale",
            "Rust or C++ for inference optimization",
        ],
        "resume_headline": "ML Engineer · NLP · PyTorch · Transformers · AWS",
        "professional_summary": (
            "ML Engineer with 4 years shipping NLP models in PyTorch. "
            "Experience fine-tuning transformers and deploying on SageMaker. "
            "Passionate about large language models."
        ),
        "cover_letter_draft": (
            "Dear Cohere Team,\n\n"
            "I am eager to join Cohere as an ML Engineer. My hands-on "
            "experience with transformer architectures and NLP pipelines "
            "makes me a strong fit for your mission.\n\n"
            "Regards,\nAmit Patel"
        ),
        "interview_questions": [
            "Explain the attention mechanism in transformers.",
            "How would you evaluate an LLM for production readiness?",
            "Describe your experience with model quantization or distillation.",
        ],
        "bilingual_pitch": (
            "EN: I'm Amit, an ML Engineer focused on NLP and large language "
            "models. I ship production transformers on PyTorch and SageMaker."
        ),
        "application_checklist": [
            "Showcase open-source NLP contributions",
            "Prepare system-design answer for LLM serving",
            "Review Cohere's API and model lineup",
            "Brush up on RLHF and alignment techniques",
        ],
    },
]

# Track decisions made during this server session
_decisions: dict[str, ActionResponse] = {}

# ---------------------------------------------------------------------------
# API endpoints
# ---------------------------------------------------------------------------


@app.get("/api/pending")
def get_pending() -> list[dict[str, Any]]:
    """Return all pending application packages that haven't been actioned."""
    actioned = set(_decisions.keys())
    return [p for p in MOCK_PACKAGES if p["session_id"] not in actioned]


@app.post("/api/action/{session_id}")
def post_action(session_id: str, body: ActionRequest) -> ActionResponse:
    """Approve or reject a pending review."""
    pkg = next((p for p in MOCK_PACKAGES if p["session_id"] == session_id), None)
    if pkg is None:
        raise HTTPException(404, f"Session {session_id} not found")
    if session_id in _decisions:
        raise HTTPException(409, f"Session {session_id} already actioned")

    decision = "approved" if body.approved else "rejected"

    # Build a mock final career review (in production this would resume the
    # ADK workflow via the Agent Runtime interrupt API).
    final_review: dict[str, Any] = {
        "id": str(uuid.uuid4())[:8],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "candidate": pkg["candidate_name"],
        "job_title": pkg["job_title"],
        "company": pkg["company"],
        "decision": decision,
        "reviewer_note": body.reviewer_note,
        "match_score": pkg["match_score"],
        "summary": (
            f"Application for {pkg['candidate_name']} → {pkg['job_title']} "
            f"at {pkg['company']} has been **{decision}**."
        ),
        "next_steps": (
            pkg["application_checklist"]
            if body.approved
            else ["Review feedback and update application materials."]
        ),
    }

    resp = ActionResponse(
        session_id=session_id,
        decision=decision,
        reviewer_note=body.reviewer_note,
        final_review=final_review,
    )
    _decisions[session_id] = resp
    return resp


# ---------------------------------------------------------------------------
# HTML dashboard
# ---------------------------------------------------------------------------

DASHBOARD_HTML = """\
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>ApplyWise AI — Career Review Dashboard</title>
<meta name="description" content="Review pending career application packages produced by the ApplyWise AI multi-agent workflow." />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet" />
<style>
/* ── Reset & Base ─────────────────────────────────────────────── */
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:      #0b0e17;
  --surface: rgba(255,255,255,.04);
  --glass:   rgba(255,255,255,.06);
  --border:  rgba(255,255,255,.08);
  --text:    #e2e8f0;
  --muted:   #8892a4;
  --accent:  #6366f1;
  --accent2: #818cf8;
  --green:   #22c55e;
  --red:     #ef4444;
  --amber:   #f59e0b;
  --radius:  16px;
  --font:    'Inter', system-ui, sans-serif;
}
html{font-size:15px}
body{
  font-family:var(--font);
  background:var(--bg);
  color:var(--text);
  min-height:100vh;
  overflow-x:hidden;
}
/* Ambient glow blobs */
body::before,body::after{
  content:'';position:fixed;border-radius:50%;pointer-events:none;
  filter:blur(120px);opacity:.18;z-index:0;
}
body::before{width:600px;height:600px;background:#6366f1;top:-120px;left:-100px}
body::after{width:500px;height:500px;background:#06b6d4;bottom:-80px;right:-60px}

/* ── Layout ──────────────────────────────────────────────────── */
.wrapper{position:relative;z-index:1;max-width:1280px;margin:0 auto;padding:2rem 1.5rem 4rem}

/* ── Header ──────────────────────────────────────────────────── */
header{text-align:center;margin-bottom:3rem}
header h1{
  font-size:2.4rem;font-weight:800;
  background:linear-gradient(135deg,#818cf8,#6366f1,#a78bfa);
  -webkit-background-clip:text;-webkit-text-fill-color:transparent;
  letter-spacing:-.02em;
}
header p{color:var(--muted);margin-top:.4rem;font-size:.95rem;font-weight:400}
.badge-row{display:flex;gap:.6rem;justify-content:center;margin-top:1rem;flex-wrap:wrap}
.badge{
  display:inline-flex;align-items:center;gap:.35rem;
  font-size:.75rem;font-weight:600;text-transform:uppercase;letter-spacing:.04em;
  padding:.35rem .75rem;border-radius:999px;
  background:rgba(99,102,241,.12);color:var(--accent2);border:1px solid rgba(99,102,241,.2);
}
.badge.green{background:rgba(34,197,94,.1);color:var(--green);border-color:rgba(34,197,94,.2)}
.badge .dot{width:6px;height:6px;border-radius:50%;background:currentColor;animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}

/* ── Cards grid ──────────────────────────────────────────────── */
#cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(370px,1fr));gap:1.5rem}
.card{
  background:var(--glass);
  backdrop-filter:blur(24px) saturate(1.4);
  -webkit-backdrop-filter:blur(24px) saturate(1.4);
  border:1px solid var(--border);
  border-radius:var(--radius);
  padding:1.6rem;
  transition:transform .25s,box-shadow .25s,border-color .25s;
  cursor:pointer;position:relative;overflow:hidden;
}
.card:hover{transform:translateY(-4px);box-shadow:0 12px 40px rgba(99,102,241,.12);border-color:rgba(99,102,241,.25)}
.card::before{
  content:'';position:absolute;inset:0;
  background:linear-gradient(135deg,rgba(99,102,241,.06),transparent 60%);
  pointer-events:none;
}
.card-header{display:flex;align-items:flex-start;justify-content:space-between;gap:1rem;margin-bottom:1rem}
.card-header h2{font-size:1.1rem;font-weight:700;line-height:1.3}
.card-header .company{color:var(--muted);font-size:.82rem;margin-top:.2rem}

/* Score ring */
.score-ring{
  flex-shrink:0;width:56px;height:56px;border-radius:50%;
  display:flex;align-items:center;justify-content:center;
  font-weight:800;font-size:1.05rem;
  border:3px solid;position:relative;
}
.score-ring.high{border-color:var(--green);color:var(--green);background:rgba(34,197,94,.08)}
.score-ring.mid{border-color:var(--amber);color:var(--amber);background:rgba(245,158,11,.08)}
.score-ring.low{border-color:var(--red);color:var(--red);background:rgba(239,68,68,.08)}

/* Tags */
.tag-row{display:flex;flex-wrap:wrap;gap:.4rem;margin-top:.6rem}
.tag{
  font-size:.7rem;font-weight:500;padding:.25rem .55rem;border-radius:6px;
  background:rgba(99,102,241,.1);color:var(--accent2);border:1px solid rgba(99,102,241,.15);
}
.tag.miss{background:rgba(239,68,68,.08);color:#f87171;border-color:rgba(239,68,68,.15)}

/* Labels */
.label{font-size:.7rem;font-weight:600;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);margin-top:1rem;margin-bottom:.3rem}

/* Headline */
.headline{
  font-size:.85rem;font-weight:500;color:var(--text);
  padding:.5rem .7rem;border-radius:8px;
  background:rgba(255,255,255,.03);border:1px solid var(--border);margin-top:.3rem;
}

/* Buttons row */
.btn-row{display:flex;gap:.6rem;margin-top:1.3rem}
.btn{
  flex:1;padding:.65rem 1rem;border:none;border-radius:10px;
  font-family:var(--font);font-size:.82rem;font-weight:600;cursor:pointer;
  display:inline-flex;align-items:center;justify-content:center;gap:.4rem;
  transition:background .2s,transform .15s,box-shadow .2s;
}
.btn:active{transform:scale(.97)}
.btn-approve{background:var(--green);color:#fff}
.btn-approve:hover{background:#16a34a;box-shadow:0 4px 20px rgba(34,197,94,.3)}
.btn-reject{background:rgba(239,68,68,.15);color:#f87171;border:1px solid rgba(239,68,68,.2)}
.btn-reject:hover{background:rgba(239,68,68,.25)}
.btn-view{background:rgba(99,102,241,.12);color:var(--accent2);border:1px solid rgba(99,102,241,.2)}
.btn-view:hover{background:rgba(99,102,241,.2)}

/* ── Spinner ─────────────────────────────────────────────────── */
.spinner{width:18px;height:18px;border:2px solid rgba(255,255,255,.2);border-top-color:#fff;border-radius:50%;animation:spin .6s linear infinite;display:none}
@keyframes spin{to{transform:rotate(360deg)}}
.btn.loading .spinner{display:inline-block}
.btn.loading span{display:none}

/* ── Slide-out modal (detail panel) ──────────────────────────── */
.overlay{
  position:fixed;inset:0;background:rgba(0,0,0,.55);backdrop-filter:blur(4px);
  z-index:100;opacity:0;pointer-events:none;transition:opacity .3s;
}
.overlay.open{opacity:1;pointer-events:auto}
.panel{
  position:fixed;top:0;right:0;width:min(560px,92vw);height:100vh;
  background:linear-gradient(180deg,#111827,#0f1729);
  border-left:1px solid var(--border);
  z-index:101;transform:translateX(100%);transition:transform .35s cubic-bezier(.4,0,.2,1);
  overflow-y:auto;padding:2rem;
}
.panel.open{transform:translateX(0)}
.panel-close{
  position:absolute;top:1.2rem;right:1.2rem;
  background:rgba(255,255,255,.06);border:1px solid var(--border);
  color:var(--text);width:36px;height:36px;border-radius:10px;
  display:flex;align-items:center;justify-content:center;
  font-size:1.1rem;cursor:pointer;transition:background .2s;
}
.panel-close:hover{background:rgba(255,255,255,.12)}
.panel h2{font-size:1.4rem;font-weight:700;margin-bottom:.2rem}
.panel .sub{color:var(--muted);font-size:.85rem;margin-bottom:1.5rem}
.panel section{margin-bottom:1.5rem}
.panel section h3{font-size:.82rem;font-weight:700;text-transform:uppercase;letter-spacing:.06em;color:var(--accent2);margin-bottom:.5rem}
.panel section p,.panel section li{font-size:.88rem;line-height:1.65;color:var(--text)}
.panel section ul{padding-left:1.2rem}
.panel section li{margin-bottom:.3rem}
.panel .cover-letter{
  white-space:pre-wrap;padding:1rem;border-radius:10px;
  background:rgba(255,255,255,.03);border:1px solid var(--border);
  font-size:.85rem;line-height:1.7;
}
.panel .pitch{
  white-space:pre-wrap;padding:1rem;border-radius:10px;
  background:rgba(99,102,241,.06);border:1px solid rgba(99,102,241,.15);
  font-size:.85rem;line-height:1.7;
}
.panel .checklist li::marker{content:'✓ ';color:var(--green)}
.panel .panel-actions{
  position:sticky;bottom:0;background:linear-gradient(0deg,#0f1729 60%,transparent);
  padding:1.5rem 0 .5rem;display:flex;gap:.6rem;
}

/* ── Final review banner ─────────────────────────────────────── */
.review-banner{
  margin-top:1rem;padding:1.2rem;border-radius:12px;
  border:1px solid var(--border);animation:fadeIn .4s;
}
.review-banner.approved{background:rgba(34,197,94,.06);border-color:rgba(34,197,94,.2)}
.review-banner.rejected{background:rgba(239,68,68,.06);border-color:rgba(239,68,68,.2)}
.review-banner h4{font-size:.9rem;font-weight:700;margin-bottom:.4rem}
.review-banner p{font-size:.82rem;color:var(--muted);line-height:1.6}
@keyframes fadeIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

/* ── Empty state ─────────────────────────────────────────────── */
.empty{text-align:center;padding:4rem 1rem;color:var(--muted)}
.empty .icon{font-size:3rem;margin-bottom:1rem}
.empty h3{font-size:1.2rem;font-weight:600;color:var(--text);margin-bottom:.4rem}

/* ── Responsive ──────────────────────────────────────────────── */
@media(max-width:480px){
  #cards{grid-template-columns:1fr}
  header h1{font-size:1.6rem}
}

/* ── Note textarea in panel ──────────────────────────────────── */
.note-input{
  width:100%;padding:.7rem;border-radius:10px;
  background:rgba(255,255,255,.04);border:1px solid var(--border);
  color:var(--text);font-family:var(--font);font-size:.85rem;
  resize:vertical;min-height:60px;margin-top:.4rem;
  transition:border-color .2s;
}
.note-input:focus{outline:none;border-color:var(--accent)}
.note-input::placeholder{color:var(--muted)}
</style>
</head>
<body>

<!-- Overlay for slide-out panel -->
<div class="overlay" id="overlay" onclick="closePanel()"></div>
<div class="panel" id="panel">
  <button class="panel-close" onclick="closePanel()" aria-label="Close">✕</button>
  <div id="panel-content"></div>
</div>

<div class="wrapper">
  <header>
    <h1>🍁 ApplyWise AI</h1>
    <p>Career Application Review Dashboard</p>
    <div class="badge-row">
      <span class="badge"><span class="dot"></span> Local Demo</span>
      <span class="badge green"><span class="dot"></span> <span id="pending-count">0</span> Pending</span>
    </div>
  </header>

  <div id="cards"></div>
</div>

<script>
/* ── State ──────────────────────────────────────────────────── */
let packages = [];
let currentPkg = null;

/* ── Helpers ─────────────────────────────────────────────────── */
const $ = s => document.querySelector(s);
const scoreClass = s => s >= 85 ? 'high' : s >= 70 ? 'mid' : 'low';

function tags(arr, cls = '') {
  return arr.map(t => `<span class="tag ${cls}">${t}</span>`).join('');
}

/* ── Fetch & Render ──────────────────────────────────────────── */
async function loadPending() {
  const res = await fetch('/api/pending');
  packages = await res.json();
  $('#pending-count').textContent = packages.length;
  renderCards();
}

function renderCards() {
  const el = $('#cards');
  if (!packages.length) {
    el.innerHTML = `
      <div class="empty" style="grid-column:1/-1">
        <div class="icon">🎉</div>
        <h3>All Caught Up</h3>
        <p>No pending application reviews. New packages will appear here.</p>
      </div>`;
    return;
  }
  el.innerHTML = packages.map(p => `
    <div class="card" onclick="openPanel('${p.session_id}')">
      <div class="card-header">
        <div>
          <h2>${p.candidate_name}</h2>
          <div class="company">${p.job_title} — ${p.company}</div>
          <div class="company" style="margin-top:2px;font-size:.75rem">${p.location}</div>
        </div>
        <div class="score-ring ${scoreClass(p.match_score)}">${p.match_score}</div>
      </div>

      <div class="label">Top Skills</div>
      <div class="tag-row">${tags(p.top_skills.slice(0, 4))}</div>

      <div class="label">Gaps</div>
      <div class="tag-row">${tags(p.missing_skills.slice(0, 3), 'miss')}</div>

      <div class="label">Resume Headline</div>
      <div class="headline">${p.resume_headline}</div>

      <div class="btn-row">
        <button class="btn btn-approve" id="approve-${p.session_id}" onclick="event.stopPropagation();doAction('${p.session_id}',true)">
          <div class="spinner"></div><span>✓ Approve</span>
        </button>
        <button class="btn btn-reject" id="reject-${p.session_id}" onclick="event.stopPropagation();doAction('${p.session_id}',false)">
          <div class="spinner"></div><span>✗ Reject</span>
        </button>
        <button class="btn btn-view" onclick="event.stopPropagation();openPanel('${p.session_id}')">
          <span>View ▸</span>
        </button>
      </div>
      <div id="banner-${p.session_id}"></div>
    </div>
  `).join('');
}

/* ── Slide-out Panel ─────────────────────────────────────────── */
function openPanel(sid) {
  const p = packages.find(x => x.session_id === sid);
  if (!p) return;
  currentPkg = p;

  $('#panel-content').innerHTML = `
    <h2>${p.candidate_name}</h2>
    <div class="sub">${p.job_title} — ${p.company} · ${p.location}</div>

    <div style="display:flex;align-items:center;gap:1rem;margin-bottom:1.5rem">
      <div class="score-ring ${scoreClass(p.match_score)}" style="width:64px;height:64px;font-size:1.2rem">${p.match_score}</div>
      <div>
        <div style="font-weight:700;font-size:1rem">Match Score</div>
        <div style="color:var(--muted);font-size:.82rem">Based on skills & experience overlap</div>
      </div>
    </div>

    <section>
      <h3>Professional Summary</h3>
      <p>${p.professional_summary}</p>
    </section>

    <section>
      <h3>Top Matching Skills</h3>
      <div class="tag-row">${tags(p.top_skills)}</div>
    </section>

    <section>
      <h3>Missing Skills</h3>
      <div class="tag-row">${tags(p.missing_skills, 'miss')}</div>
    </section>

    <section>
      <h3>Interview Questions</h3>
      <ul>${p.interview_questions.map(q => `<li>${q}</li>`).join('')}</ul>
    </section>

    <section>
      <h3>Cover Letter Draft</h3>
      <div class="cover-letter">${p.cover_letter_draft}</div>
    </section>

    <section>
      <h3>Bilingual Elevator Pitch</h3>
      <div class="pitch">${p.bilingual_pitch}</div>
    </section>

    <section>
      <h3>Application Checklist</h3>
      <ul class="checklist">${p.application_checklist.map(c => `<li>${c}</li>`).join('')}</ul>
    </section>

    <section>
      <h3>Reviewer Note</h3>
      <textarea class="note-input" id="panel-note" placeholder="Add an optional note for the candidate…"></textarea>
    </section>

    <div class="panel-actions">
      <button class="btn btn-approve" style="flex:1" id="panel-approve" onclick="panelAction(true)">
        <div class="spinner"></div><span>✓ Approve Package</span>
      </button>
      <button class="btn btn-reject" style="flex:1" id="panel-reject" onclick="panelAction(false)">
        <div class="spinner"></div><span>✗ Reject Package</span>
      </button>
    </div>
    <div id="panel-banner"></div>
  `;

  $('#overlay').classList.add('open');
  $('#panel').classList.add('open');
}

function closePanel() {
  $('#overlay').classList.remove('open');
  $('#panel').classList.remove('open');
  currentPkg = null;
}

/* ── Actions ─────────────────────────────────────────────────── */
async function doAction(sid, approved) {
  const btnId = approved ? `approve-${sid}` : `reject-${sid}`;
  const btn = document.getElementById(btnId);
  btn.classList.add('loading');

  try {
    const res = await fetch(`/api/action/${sid}`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({approved, reviewer_note: ''})
    });
    const data = await res.json();
    showBanner(`banner-${sid}`, data);
    // Refresh after brief delay so user sees the banner
    setTimeout(loadPending, 1800);
  } catch (e) {
    console.error(e);
  } finally {
    btn.classList.remove('loading');
  }
}

async function panelAction(approved) {
  if (!currentPkg) return;
  const sid = currentPkg.session_id;
  const btnId = approved ? 'panel-approve' : 'panel-reject';
  const btn = document.getElementById(btnId);
  btn.classList.add('loading');
  const note = document.getElementById('panel-note')?.value || '';

  try {
    const res = await fetch(`/api/action/${sid}`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({approved, reviewer_note: note})
    });
    const data = await res.json();
    showBanner('panel-banner', data);
    // Also update the card if visible
    showBanner(`banner-${sid}`, data);
    setTimeout(() => { closePanel(); loadPending(); }, 2000);
  } catch (e) {
    console.error(e);
  } finally {
    btn.classList.remove('loading');
  }
}

function showBanner(elId, data) {
  const el = document.getElementById(elId);
  if (!el) return;
  const cls = data.decision === 'approved' ? 'approved' : 'rejected';
  const icon = data.decision === 'approved' ? '✅' : '❌';
  el.innerHTML = `
    <div class="review-banner ${cls}">
      <h4>${icon} ${data.final_review.summary}</h4>
      ${data.reviewer_note ? `<p><strong>Note:</strong> ${data.reviewer_note}</p>` : ''}
      <p style="margin-top:.4rem"><strong>Next steps:</strong> ${data.final_review.next_steps.join(' · ')}</p>
    </div>
  `;
}

/* ── Keyboard shortcut ───────────────────────────────────────── */
document.addEventListener('keydown', e => { if (e.key === 'Escape') closePanel(); });

/* ── Init ────────────────────────────────────────────────────── */
loadPending();
</script>
</body>
</html>
"""


@app.get("/", response_class=HTMLResponse)
def dashboard() -> str:
    """Serve the glassmorphism review dashboard."""
    return DASHBOARD_HTML


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8501, reload=True)
