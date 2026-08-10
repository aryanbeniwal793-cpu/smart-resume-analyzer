import { useState } from "react";
import axios from "axios";

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
    <div className="analyzer-container">
      <h1 className="analyzer-title">Smart Resume Analyzer</h1>

      <input
        type="file"
        accept=".pdf"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <br /><br />

      <button onClick={uploadResume}>
        Upload Resume
      </button>

      <hr />

      <h2>Parsed Resume</h2>

      {parsed && (
        <div>
          <p><strong>Name:</strong> {parsed.name}</p>
          <p><strong>Email:</strong> {parsed.email}</p>
          <p><strong>Phone:</strong> {parsed.phone}</p>

          <p><strong>Skills:</strong></p>

          <ul>
            {parsed.skills.map((skill, index) => (
              <li key={index}>{skill}</li>
            ))}
          </ul>
        </div>
      )}

      <hr />

      <h2>Paste Job Description</h2>

      <textarea
        rows="10"
        cols="60"
        placeholder="Paste Job Description here..."
        value={jobDescription}
        onChange={(e) => setJobDescription(e.target.value)}
      />

      <br /><br />

      <button onClick={analyzeJD}>
        Analyze JD
      </button>

      <hr />

      <h2>Required Skills</h2>

      <ul>
        {jdSkills.map((skill, index) => (
          <li key={index}>{skill}</li>
        ))}
      </ul>

      {ats && (
        <div className="section">

        <h2>ATS Score</h2>

        <div className="ats-score">
        {ats.score}%
        </div>

        <h3>Match Rating</h3>
        <p>{ats.rating}</p>

        <ul className="skill-list matched">
        {ats.matched.map((skill, index) => (
        <li key={index}>✓ {skill}</li>
      ))}
    </ul>

    <h3>Missing Skills</h3>

    <ul className="skill-list missing">
      {ats.missing.map((skill, index) => (
        <li key={index}>✗ {skill}</li>
      ))}
    </ul>

    <h3>Resume Suggestions</h3>

    <ul className="suggestions">
      {ats.suggestions.map((suggestion, index) => (
        <li key={index}>→ {suggestion}</li>
      ))}
    </ul>

  </div>
)}

      <hr />

      <h2>Extracted Text</h2>

      <pre>{text}</pre>
    </div>
  );
}

export default App;