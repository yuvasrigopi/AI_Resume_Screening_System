from services.skill_extractor import extract_skills


def calculate_similarity(resume_text, job_description):
    """
    Calculate similarity based on matching skills.
    Returns percentage and missing skills.
    """

    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(job_description)

    if len(jd_skills) == 0:
        return 0, []

    matched = []

    missing = []

    for skill in jd_skills:

        if skill in resume_skills:
            matched.append(skill)
        else:
            missing.append(skill)

    similarity = round((len(matched) / len(jd_skills)) * 100, 2)

    return similarity, missing