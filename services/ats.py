from services.skill_extractor import extract_skills
from services.similarity import calculate_similarity


def calculate_ats_score(resume_text, job_description):
    """
    Calculate ATS score based on:
    1. Resume length (20%)
    2. Skill match (60%)
    3. Resume completeness (20%)
    """

    score = 0

    # -------------------------
    # Resume Length (20 Marks)
    # -------------------------
    words = len(resume_text.split())

    if words >= 500:
        score += 20
    elif words >= 300:
        score += 15
    elif words >= 150:
        score += 10
    else:
        score += 5

    # -------------------------
    # Skill Match (60 Marks)
    # -------------------------
    similarity, missing_skills = calculate_similarity(
        resume_text,
        job_description
    )

    score += similarity * 0.6

    # -------------------------
    # Resume Completeness (20 Marks)
    # -------------------------
    skills = extract_skills(resume_text)

    if len(skills) >= 10:
        score += 20
    elif len(skills) >= 7:
        score += 15
    elif len(skills) >= 4:
        score += 10
    else:
        score += 5

    return round(min(score, 100), 2)