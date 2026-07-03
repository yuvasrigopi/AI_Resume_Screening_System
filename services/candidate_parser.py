import re


def extract_name(text):
    """
    Extract candidate name from resume.
    Assumes the first non-empty line is the name.
    """

    lines = text.split("\n")

    for line in lines:

        line = line.strip()

        if len(line) > 2 and len(line.split()) <= 4:
            return line.title()

    return "Not Found"


def extract_email(text):
    """
    Extract email address.
    """

    pattern = r'[\w\.-]+@[\w\.-]+\.\w+'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_phone(text):
    """
    Extract Indian mobile number.
    """

    pattern = r'(\+91[- ]?)?[6-9]\d{9}'

    match = re.search(pattern, text)

    if match:
        return match.group()

    return "Not Found"


def extract_experience(text):
    """
    Extract years of experience if mentioned.
    """

    pattern = r'(\d+)\+?\s*(years|year|yrs|yr)'

    matches = re.findall(pattern, text, flags=re.IGNORECASE)

    if matches:
        return matches[0][0] + " Years"

    return "Fresher"


def extract_education(text):
    """
    Detect highest qualification.
    """

    education_keywords = [

        "PhD",
        "M.Tech",
        "M.E",
        "MBA",
        "MCA",
        "M.Sc",
        "B.Tech",
        "B.E",
        "BCA",
        "B.Sc",
        "Diploma"

    ]

    for degree in education_keywords:

        if degree.lower() in text.lower():
            return degree

    return "Not Mentioned"