# 📄 Smart Resume Analyzer

A full-stack web application that analyzes resumes by extracting key information such as contact details and technical skills from PDF resumes.

This project is being built as a step-by-step learning journey using **React** and **FastAPI**, with future enhancements including ATS scoring, job description matching, and AI-powered resume analysis.

---

## 🚀 Features

### ✅ Current Features

- Upload PDF resumes
- Extract text from PDF files
- Parse:
  - Name
  - Email
  - Phone Number
  - Technical Skills
- Display extracted information in a React frontend

---

## 🛠️ Tech Stack

### Frontend
- React
- Vite
- Axios

### Backend
- FastAPI
- PyMuPDF (fitz)
- Python

---

## 📂 Project Structure

```
smart-resume-analyzer/
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── main.py
│   ├── parser.py
│   ├── skills.py
│   └── requirements.txt
│
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/smart-resume-analyzer.git
```

### Backend

```bash
cd backend

pip install -r requirements.txt

python -m uvicorn main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

## 📸 Current Output

After uploading a resume, the application displays:

- Parsed Name
- Email
- Phone Number
- Skills
- Complete Extracted Resume Text

---

## 📈 Roadmap

- [x] Resume Upload
- [x] PDF Text Extraction
- [x] Resume Parsing
- [ ] Job Description Upload
- [ ] ATS Skill Matching
- [ ] ATS Score Calculation
- [ ] Resume Improvement Suggestions
- [ ] Modern Dashboard UI
- [ ] AI-powered Resume Analysis
- [ ] Resume Download Report

---

## 📚 Learning Goals

This project is focused on learning:

- React
- FastAPI
- REST APIs
- Resume Parsing
- Regular Expressions (Regex)
- Full Stack Development
- AI Integration (Upcoming)

---
## 📅 Development Progress

| Day | Progress |
|-----|----------|
| Day 1 | Project setup with React and FastAPI |
| Day 2 | Implemented PDF upload and text extraction |
| Day 3 | Added resume parsing (name, email, phone, skills) |
| Day 4 | Coming Soon |

## 🤝 Contributing

Suggestions and improvements are welcome. Feel free to fork the repository and submit a pull request.

---

## 📄 License

This project is licensed under the MIT License.