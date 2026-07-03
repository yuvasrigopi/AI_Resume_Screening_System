from utils.constants import SKILLS


def extract_skills(text):
    """
    Extract skills from resume or Job Description.
    """

    if not text:
        return []

    text = text.lower()

    extracted = []

    for skill in SKILLS:

        if skill.lower() in text:

            extracted.append(skill)

    return sorted(list(set(extracted)))
    return sorted(list(set(skills)))