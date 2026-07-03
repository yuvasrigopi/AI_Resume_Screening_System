from services.candidate_parser import (
    extract_name,
    extract_email,
    extract_phone,
    extract_experience,
    extract_education
)

from services.skill_extractor import extract_skills
from services.similarity import calculate_similarity
from services.ats import calculate_ats_score
from utils.helper import generate_report


def get_recommendation(ats_score):

    if ats_score >= 85:
        return "Highly Recommended"

    elif ats_score >= 70:
        return "Recommended"

    elif ats_score >= 50:
        return "Can be Considered"

    else:
        return "Needs Improvement"


def analyze_resume(resume_text, filename, job_description):

    # -------------------------------
    # Candidate Details
    # -------------------------------

    name = extract_name(resume_text)

    email = extract_email(resume_text)

    phone = extract_phone(resume_text)

    experience = extract_experience(resume_text)

    education = extract_education(resume_text)

    # -------------------------------
    # Resume Skills
    # -------------------------------

    skills = extract_skills(resume_text)

    # -------------------------------
    # Match Percentage & Missing Skills
    # -------------------------------

    similarity, missing_skills = calculate_similarity(
        resume_text,
        job_description
    )

    # -------------------------------
    # ATS Score
    # -------------------------------

    ats_score = calculate_ats_score(
        resume_text,
        job_description
    )

    # -------------------------------
    # Recommendation
    # -------------------------------

    recommendation = get_recommendation(ats_score)

    # -------------------------------
    # Generate PDF Report
    # -------------------------------

    report = generate_report(
        filename,
        ats_score,
        similarity,
        skills,
        missing_skills,
        recommendation
    )

    # -------------------------------
    # Final Result
    # -------------------------------

    return {

        "filename": filename,

        "name": name,

        "email": email,

        "phone": phone,

        "education": education,

        "experience": experience,

        "skills": skills,

        "missing_skills": missing_skills,

        "similarity": similarity,

        "ats_score": ats_score,

        "recommendation": recommendation,

        "report": report

    }