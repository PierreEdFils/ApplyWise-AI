import re
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP Server
mcp = FastMCP("ApplyWiseTools")

# Predefined list of common tech keywords for simple local extraction
TECH_KEYWORDS = {
    "react", "angular", "vue", "javascript", "typescript", "html", "css",
    "python", "ruby", "rails", "node", "express", "django", "flask", "fastapi",
    "java", "spring", "c++", "c#", "dotnet", "go", "rust", "php", "laravel",
    "aws", "gcp", "azure", "docker", "kubernetes", "terraform", "ansible", "ci/cd",
    "sql", "postgresql", "mysql", "mongodb", "redis", "graphql", "rest api",
    "agile", "scrum", "kanban", "product management", "product owner",
    "bilingual", "french", "english", "communication", "leadership", "teamwork"
}

@mcp.tool()
def validate_inputs(jd: str, resume: str) -> dict:
    """Validates that the job description and candidate profile are not empty and meet basic length requirements.

    Args:
        jd: The job description text.
        resume: The candidate profile or resume text.

    Returns:
        A dict containing 'valid' (bool) and 'errors' (list of str).
    """
    errors = []
    if not jd.strip():
        errors.append("Job description cannot be empty.")
    elif len(jd.strip()) < 100:
        errors.append("Job description seems too short (minimum 100 characters).")
        
    if not resume.strip():
        errors.append("Candidate profile/resume cannot be empty.")
    elif len(resume.strip()) < 100:
        errors.append("Candidate profile/resume seems too short (minimum 100 characters).")
        
    return {
        "valid": len(errors) == 0,
        "errors": errors
    }

@mcp.tool()
def extract_keywords(text: str) -> list[str]:
    """Extracts technical skills, methodologies, and language keywords from a text.

    Args:
        text: The text (job description or resume) to extract keywords from.

    Returns:
        A list of matching keywords found in the text.
    """
    text_lower = text.lower()
    found_keywords = set()
    
    # Check for exact word matches from our predefined list
    for kw in TECH_KEYWORDS:
        # Use word boundaries to avoid partial matches (e.g., 'go' in 'good')
        pattern = rf"\b{re.escape(kw)}\b"
        if re.search(pattern, text_lower):
            found_keywords.add(kw)
            
    # Also look for years of experience patterns
    exp_matches = re.findall(r"(\d+)\s*\+\s*years", text_lower)
    for match in exp_matches:
        found_keywords.add(f"{match}+ years experience")
        
    return sorted(list(found_keywords))

@mcp.tool()
def calculate_match_score(jd_keywords: list[str], resume_keywords: list[str]) -> dict:
    """Calculates a match score between a job description and a candidate's resume based on overlapping keywords.

    Args:
        jd_keywords: The list of keywords extracted from the job description.
        resume_keywords: The list of keywords extracted from the resume.

    Returns:
        A dict containing the overall score (0-100), overlapping keywords, and missing keywords.
    """
    if not jd_keywords:
        return {"score": 0, "match_percentage": 0, "overlap": [], "missing": []}
        
    jd_set = set(k.lower() for k in jd_keywords)
    resume_set = set(k.lower() for k in resume_keywords)
    
    overlap = jd_set.intersection(resume_set)
    missing = jd_set.difference(resume_set)
    
    # Calculate score weighted by type of keyword
    # Language keywords and core tech keywords carry higher weight
    score = int((len(overlap) / len(jd_set)) * 100)
    
    return {
        "score": score,
        "match_percentage": score,
        "overlap": sorted(list(overlap)),
        "missing": sorted(list(missing))
    }

@mcp.tool()
def detect_missing_skills(jd_keywords: list[str], resume_keywords: list[str]) -> list[str]:
    """Identifies skills required by the job description that are missing from the candidate's resume.

    Args:
        jd_keywords: The list of keywords extracted from the job description.
        resume_keywords: The list of keywords extracted from the resume.

    Returns:
        A list of missing skills.
    """
    jd_set = set(k.lower() for k in jd_keywords)
    resume_set = set(k.lower() for k in resume_keywords)
    missing = jd_set.difference(resume_set)
    return sorted(list(missing))

@mcp.tool()
def format_resume_bullet(bullet: str, action_verb: str, result: str) -> str:
    """Formats a resume bullet point using the action-oriented Google formula: Accomplished [X] as measured by [Y], by doing [Z].

    Args:
        bullet: The original resume bullet or achievement description.
        action_verb: A strong action verb (e.g., 'Optimized', 'Conçu', 'Architected').
        result: The measurable impact or outcome (e.g., 'reducing load times by 20%').

    Returns:
        The formatted resume bullet point.
    """
    clean_bullet = bullet.strip().rstrip('.')
    # Remove leading hyphens or bullet points if present
    clean_bullet = re.sub(r"^[\s•\-\*]+", "", clean_bullet)
    
    # Capitalize action verb
    verb = action_verb.strip().capitalize()
    res = result.strip()
    
    return f"{verb} {clean_bullet[0].lower()}{clean_bullet[1:]}, resulting in {res}."

@mcp.tool()
def generate_checklist(jd_text: str) -> list[str]:
    """Generates a tailored application checklist based on requirements parsed from the job description.

    Args:
        jd_text: The full text of the job description.

    Returns:
        A list of checklist items.
    """
    jd_lower = jd_text.lower()
    checklist = [
        "Tailor resume resume headline and summary",
        "Refine achievement-based bullet points",
        "Draft tailored cover letter"
      ]
    
    # Add conditional tasks based on JD content
    if "bilingual" in jd_lower or "french" in jd_lower or "français" in jd_lower:
      checklist.append("Verify French technical vocabulary and practice bilingual pitch transitions")
      checklist.append("Proofread bilingual cover letter formatting")
      
    if "portfolio" in jd_lower or "github" in jd_lower:
      checklist.append("Update GitHub profile and add link to relevant repositories")
      
    if "degree" in jd_lower or "b.sc" in jd_lower or "university" in jd_lower:
      checklist.append("Confirm educational credentials on resume")
      
    if "certificat" in jd_lower or "certified" in jd_lower:
      checklist.append("Ensure relevant professional certifications are highlighted")
      
    checklist.append("Perform final proofreading of the application package")
    return checklist

if __name__ == "__main__":
    mcp.run()
