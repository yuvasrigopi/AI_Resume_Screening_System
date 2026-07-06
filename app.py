from flask import Flask, render_template, request
import os

from werkzeug.utils import secure_filename

from services.pdf_parser import extract_text
from services.resume_analyzer import analyze_resume

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
REPORT_FOLDER = "reports"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(REPORT_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    resumes = request.files.getlist("resumes")

    job_description = request.form.get("job_description", "").strip()

    if not resumes or resumes[0].filename == "":
        return "Please upload at least one resume."

    if job_description == "":
        return "Please enter a Job Description."

    results = []

    for resume in resumes:

        filename = secure_filename(resume.filename)

        filepath = os.path.join(
            app.config["UPLOAD_FOLDER"],
            filename
        )

        resume.save(filepath)

        resume_text = extract_text(filepath)

        result = analyze_resume(
            resume_text,
            filename,
            job_description
        )

        results.append(result)

    results = sorted(
        results,
        key=lambda x: x["similarity"],
        reverse=True
    )

    for i, result in enumerate(results):
        result["rank"] = i + 1

    return render_template(
        "result.html",
        results=results
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port, debug=False)