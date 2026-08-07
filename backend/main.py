from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from parser import parse_resume
from ats import calculate_score
import fitz
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Backend is running!"}


@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    pdf = fitz.open(stream=await file.read(), filetype="pdf")

    text = ""
    for page in pdf:
        text += page.get_text()

    parsed_data = parse_resume(text)

    return {
        "filename": file.filename,
        "text": text,
        "parsed": parsed_data
    }


@app.post("/analyze-jd")
async def analyze_jd(
    file: UploadFile = File(...),
    job_description: str = Form(...)
):
    # Read Resume
    pdf = fitz.open(stream=await file.read(), filetype="pdf")

    resume_text = ""
    for page in pdf:
        resume_text += page.get_text()

    resume_data = parse_resume(resume_text)

    # Skills Database
    skills_db = [
        "Python",
        "Java",
        "C",
        "C++",
        "SQL",
        "React",
        "Node",
        "JavaScript",
        "Machine Learning",
        "HTML",
        "CSS",
        "Git",
        "FastAPI"
    ]

    # Extract JD Skills
    jd_skills = []

    jd_lines = [line.strip().lower() for line in job_description.splitlines()]

    for skill in skills_db:
        if skill.lower() in jd_lines:
            jd_skills.append(skill)

    # Calculate ATS Score
    ats = calculate_score(
        resume_data["skills"],
        jd_skills
    )

    # Debug Prints
    print("Resume Skills:", resume_data["skills"])
    print("JD Skills:", jd_skills)
    print("ATS:", ats)

    return {
        "resume": resume_data,
        "jd_skills": jd_skills,
        "ats": ats
    }