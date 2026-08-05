import { useState } from "react";
import axios from "axios";

function App() {
  const [file, setFile] = useState(null);
  const [text, setText] = useState("");
  const [parsed, setParsed] = useState(null);

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

  return (
    <div style={{ padding: 30 }}>
      <h1>Smart Resume Analyzer</h1>

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

      <h2>Extracted Text</h2>

      <pre>{text}</pre>
    </div>
  );
}

export default App;