from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from parser import parse_resume
import fitz

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
async def analyze_jd(data: dict):
    text = data["job_description"]

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

    found = []

    for skill in skills_db:
        if skill.lower() in text.lower():
            found.append(skill)

    return {
        "jd_skills": found
    }
