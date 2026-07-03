import os

# ==========================
# Project Folders
# ==========================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

REPORT_FOLDER = os.path.join(BASE_DIR, "reports")

JOB_DESCRIPTION_FOLDER = os.path.join(BASE_DIR, "job_descriptions")


# ==========================
# Allowed File Types
# ==========================

ALLOWED_EXTENSIONS = {"pdf"}


# ==========================
# Skill Database
# ==========================

SKILLS = [

    # Programming Languages
    "Python",
    "Java",
    "C",
    "C++",
    "JavaScript",
    "SQL",
    "R",

    # AI / ML
    "Machine Learning",
    "Deep Learning",
    "Artificial Intelligence",
    "Data Science",
    "NLP",
    "Computer Vision",

    # Libraries
    "TensorFlow",
    "PyTorch",
    "Scikit-learn",
    "Pandas",
    "NumPy",
    "Matplotlib",

    # Web
    "Flask",
    "Django",
    "HTML",
    "CSS",
    "Bootstrap",

    # Database
    "MySQL",
    "MongoDB",
    "PostgreSQL",

    # Cloud
    "AWS",
    "Azure",
    "Docker",
    "Git",
    "GitHub",

    # Soft Skills
    "Communication",
    "Leadership",
    "Problem Solving",
    "Teamwork",
    "Time Management"

]