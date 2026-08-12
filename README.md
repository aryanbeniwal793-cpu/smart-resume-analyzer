# 📄 Smart Resume Analyzer

A full-stack web application that analyzes resumes against job descriptions to calculate an ATS match score, identify matched and missing skills, and provide resume improvement suggestions.

The project is built using React and FastAPI and demonstrates PDF processing, resume parsing, REST API integration, skill extraction, ATS scoring, validation, and error handling.

---

## 🚀 Features

- Upload and analyze PDF resumes
- Validate uploaded file types
- Extract text from PDF resumes
- Extract resume information:
  - Name
  - Email
  - Phone number
  - Technical skills
- Paste a job description
- Extract required technical skills from the job description
- Compare resume skills with job requirements
- Calculate ATS match score
- Display ATS rating
- Display matched skills
- Display missing skills
- Generate resume improvement suggestions
- Display extracted resume text
- Handle invalid file uploads
- Responsive frontend interface
- Frontend-backend integration using REST APIs

---

## 🛠️ Tech Stack

### Frontend

- React
- Vite
- JavaScript
- Axios
- CSS

### Backend

- Python
- FastAPI
- PyMuPDF (`fitz`)
- Regular Expressions (`re`)

### Development Tools

- Git
- GitHub
- VS Code

---

## 🏗️ System Architecture

```text
                    User
                     │
                     ▼
              React Frontend
                     │
                     │ HTTP Requests
                     ▼
              FastAPI Backend
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
    PDF Resume Parser      JD Skill Extraction
          │                     │
          ▼                     ▼
     Resume Skills         Required Skills
          │                     │
          └──────────┬──────────┘
                     ▼
                ATS Analyzer
                     │
          ┌──────────┼──────────┐
          │          │          │
          ▼          ▼          ▼
       Score      Matched     Missing
                    Skills      Skills
                     │
                     ▼
              Suggestions
                     │
                     ▼
              React Results UI
```

---

## 📂 Project Structure

```text
smart-resume-analyzer/
│
├── backend/
│   ├── main.py
│   ├── parser.py
│   ├── ats.py
│   ├── skills.py
│   ├── requirements.txt
│   └── .gitignore
│
├── frontend/
│   ├── src/
│   │   ├── assets/
│   │   ├── api.js
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── docs/
│
├── .gitignore
└── README.md
```

---

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/aryanbeniwal793-cpu/smart-resume-analyzer.git
cd smart-resume-analyzer
```

---

## 🐍 Backend Setup

Navigate to the backend:

```bash
cd backend
```

Create and activate a virtual environment:

### Windows

```powershell
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Start the FastAPI server:

```powershell
python -m uvicorn main:app --reload
```

Backend will run at:

```text
http://127.0.0.1:8000
```

---

## ⚛️ Frontend Setup

Open another terminal and navigate to the frontend:

```powershell
cd frontend
```

Install dependencies:

```powershell
npm install
```

Start the development server:

```powershell
npm run dev
```

Frontend will normally run at:

```text
http://localhost:5173
```

---

## 🔌 API Endpoints

### `GET /`

Checks whether the backend is running.

Example response:

```json
{
  "message": "Backend is running!"
}
```

### `POST /upload`

Uploads a PDF resume and extracts:

- Resume text
- Name
- Email
- Phone number
- Skills

### `POST /analyze-jd`

Analyzes a resume against a supplied job description.

The endpoint returns:

- Parsed resume information
- Required job-description skills
- ATS score
- ATS rating
- Matched skills
- Missing skills
- Resume improvement suggestions

---

## 📊 ATS Scoring

The ATS score is calculated by comparing the skills found in the resume against the skills required by the job description.

```text
ATS Score =
(Matched Required Skills / Total Required Skills) × 100
```

### Rating System

| Score | Rating |
|---|---|
| 80–100% | Excellent |
| 60–79% | Good |
| 40–59% | Needs Improvement |
| 0–39% | Low Match |

The system also identifies which required skills are missing and generates suggestions based on those missing skills.

---

## 🧪 Testing

The application was tested across multiple scenarios, including:

- Successful PDF resume upload
- Resume parsing
- Job description skill extraction
- ATS score calculation
- Matched skill detection
- Missing skill detection
- Resume suggestions
- Invalid file upload handling
- Different ATS score scenarios
- Frontend-backend API communication
- Error handling

All implemented test cases passed successfully.

---

## 🖥️ Application Workflow

1. Upload a resume in PDF format.
2. The backend extracts text from the resume.
3. Resume information and technical skills are parsed.
4. Paste a job description.
5. The backend extracts required technical skills.
6. Resume skills are compared against required skills.
7. ATS match score is calculated.
8. Matched and missing skills are displayed.
9. Resume improvement suggestions are generated.

---

## 📸 Screenshots

### Resume Upload

Add a screenshot of the resume upload interface here.

### Job Description Analysis

Add a screenshot of the job description and required skills section here.

### ATS Analysis Results

Add a screenshot showing:

- ATS score
- Rating
- Matched skills
- Missing skills
- Resume suggestions

---

## 📚 What I Learned

Through this project, I worked with:

- React component development
- React state management
- API integration using Axios
- FastAPI REST APIs
- File uploads with FastAPI
- PDF text extraction using PyMuPDF
- Resume parsing
- Regular expressions
- Skill extraction
- ATS scoring algorithms
- Frontend-backend communication
- CORS configuration
- Input validation
- Error handling
- Git and GitHub workflow
- Full-stack project structure

---

## 🗺️ Future Improvements

Possible future improvements include:

- AI-powered resume analysis
- More advanced skill extraction
- Support for DOCX resumes
- User authentication
- Resume analysis history
- Downloadable ATS reports
- Improved ATS scoring using semantic matching
- Cloud deployment
- Database integration
- More advanced resume recommendations

---

## 🎯 Project Goal

The goal of this project is to build a practical full-stack application while understanding how resume parsing, job-description analysis, ATS scoring, REST APIs, and frontend-backend integration work together in a real-world application.

---

## 👨‍💻 Author

**Aryan Beniwal**

BTech Cyber Security Student

GitHub:

https://github.com/aryanbeniwal793-cpu