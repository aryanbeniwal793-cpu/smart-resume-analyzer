from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from parser import parse_resume
from ats import calculate_score
import fitz
import re

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://localhost:5174",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Backend is running!"}


@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        return {
            "error": "Only PDF files are supported."
        }

    pdf = fitz.open(
        stream=await file.read(),
        filetype="pdf"
    )

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
    if file.content_type != "application/pdf":
        return {
            "error": "Only PDF files are supported."
        }

    if not job_description.strip():
        return {
            "error": "Job description cannot be empty."
        }

    pdf = fitz.open(
        stream=await file.read(),
        filetype="pdf"
    )

    resume_text = ""

    for page in pdf:
        resume_text += page.get_text()

    resume_data = parse_resume(resume_text)

    skills_db = [
        "Python",
        "Java",
        "C",
        "C++",
        "C#",
        "SQL",
        "React",
        "Node.js",
        "Node",
        "JavaScript",
        "TypeScript",
        "Machine Learning",
        "Deep Learning",
        "HTML",
        "CSS",
        "Git",
        "GitHub",
        "FastAPI",
        "Django",
        "Flask",
        "Docker",
        "Kubernetes",
        "AWS",
        "Azure",
        "GCP",
        "MongoDB",
        "MySQL",
        "PostgreSQL",
        "Redis",
        "Kotlin",
        "Android",
        "Swift",
        "iOS",
        "Flutter",
        "React Native",
        "TensorFlow",
        "PyTorch",
        "Linux"
    ]

    print("JD RECEIVED:", repr(job_description))

    jd_skills = []

    jd_text = job_description.lower()

    for skill in skills_db:
        pattern = r"(?<!\w)" + re.escape(skill.lower()) + r"(?!\w)"

        if re.search(pattern, jd_text):
            jd_skills.append(skill)

    ats = calculate_score(
        resume_data["skills"],
        jd_skills
    )

    print("Resume Skills:", resume_data["skills"])
    print("JD Skills:", jd_skills)
    print("ATS:", ats)

    return {
        "resume": resume_data,
        "jd_skills": jd_skills,
        "ats": ats
    }