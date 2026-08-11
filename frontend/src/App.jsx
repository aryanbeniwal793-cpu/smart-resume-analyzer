import { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [text, setText] = useState("");
  const [parsed, setParsed] = useState(null);

  const [jobDescription, setJobDescription] = useState("");
  const [jdSkills, setJdSkills] = useState([]);

  const [ats, setATS] = useState(null);

  const uploadResume = async () => {
    if (!file) {
      alert("Please select a PDF first!");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/upload",
        formData
      );

      setText(res.data.text);
      setParsed(res.data.parsed);
    } catch (err) {
      console.error(err);
      alert("Upload failed!");
    }
  };

  const analyzeJD = async () => {
    if (!file) {
      alert("Please upload/select a resume first!");
      return;
    }

    if (!jobDescription.trim()) {
      alert("Please enter a job description!");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_description", jobDescription);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/analyze-jd",
        formData
      );

      setJdSkills(response.data.jd_skills);
      setATS(response.data.ats);
    } catch (err) {
      console.error(err);
      alert("JD analysis failed!");
    }
  };

  return (
    <div className="app">

      {/* Header */}
      <header className="header">
        <h1>Smart Resume Analyzer</h1>
        <p>Analyze your resume against a job description</p>
      </header>

      {/* Resume Upload */}
      <section className="card">
        <h2>📄 Upload Resume</h2>

        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setFile(e.target.files[0])}
        />

        {file && (
          <p className="file-name">
            Selected: {file.name}
          </p>
        )}

        <button onClick={uploadResume}>
          Upload Resume
        </button>
      </section>

      {/* Parsed Resume */}
      {parsed && (
        <section className="card">
          <h2>👤 Parsed Resume</h2>

          <div className="resume-info">
            <p>
              <strong>Name:</strong> {parsed.name}
            </p>

            <p>
              <strong>Email:</strong> {parsed.email}
            </p>

            <p>
              <strong>Phone:</strong> {parsed.phone}
            </p>
          </div>

          <h3>Skills</h3>

          <div className="skill-container">
            {parsed.skills.map((skill, index) => (
              <span className="skill-tag" key={index}>
                {skill}
              </span>
            ))}
          </div>
        </section>
      )}

      {/* Job Description */}
      <section className="card">
        <h2>💼 Job Description</h2>

        <textarea
          rows="10"
          placeholder="Paste the job description here..."
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
        />

        <button onClick={analyzeJD}>
          Analyze Job Description
        </button>
      </section>

      {/* Required Skills */}
      {jdSkills.length > 0 && (
        <section className="card">
          <h2>🎯 Required Skills</h2>

          <div className="skill-container">
            {jdSkills.map((skill, index) => (
              <span className="skill-tag required" key={index}>
                {skill}
              </span>
            ))}
          </div>
        </section>
      )}

      {/* ATS Results */}
      {ats && (
        <section className="results">

          <h2 className="results-title">
            ATS Analysis Results
          </h2>

          {/* Score */}
          <div className="score-card">

            <div className="score-circle">
              <span>{ats.score}%</span>
            </div>

            <div>
              <h3>ATS Match Score</h3>
              <p className="rating">
                {ats.rating}
              </p>
            </div>

          </div>

          {/* Statistics */}
          <div className="stats">

            <div className="stat-card">
              <h3>{ats.matched.length}</h3>
              <p>Matched Skills</p>
            </div>

            <div className="stat-card">
              <h3>{ats.missing.length}</h3>
              <p>Missing Skills</p>
            </div>

            <div className="stat-card">
              <h3>{jdSkills.length}</h3>
              <p>Required Skills</p>
            </div>

          </div>

          {/* Matched and Missing */}
          <div className="skill-sections">

            <div className="result-card matched-card">
              <h3>✓ Matched Skills</h3>

              {ats.matched.length > 0 ? (
                <ul>
                  {ats.matched.map((skill, index) => (
                    <li key={index}>
                      ✓ {skill}
                    </li>
                  ))}
                </ul>
              ) : (
                <p>No matching skills found.</p>
              )}
            </div>

            <div className="result-card missing-card">
              <h3>✗ Missing Skills</h3>

              {ats.missing.length > 0 ? (
                <ul>
                  {ats.missing.map((skill, index) => (
                    <li key={index}>
                      ✗ {skill}
                    </li>
                  ))}
                </ul>
              ) : (
                <p>No missing skills!</p>
              )}
            </div>

          </div>

          {/* Suggestions */}
          <div className="result-card suggestions-card">

            <h3>💡 Resume Improvement Suggestions</h3>

            {ats.suggestions.length > 0 ? (
              <ul>
                {ats.suggestions.map((suggestion, index) => (
                  <li key={index}>
                    → {suggestion}
                  </li>
                ))}
              </ul>
            ) : (
              <p>
                Great! No additional suggestions at this time.
              </p>
            )}

          </div>

        </section>
      )}

      {/* Extracted Text */}
      {text && (
        <section className="card">

          <details>
            <summary>
              📃 View Extracted Resume Text
            </summary>

            <pre className="extracted-text">
              {text}
            </pre>

          </details>

        </section>
      )}

      <footer>
        <p>Smart Resume Analyzer • React + FastAPI</p>
      </footer>

    </div>
  );
}

export default App;