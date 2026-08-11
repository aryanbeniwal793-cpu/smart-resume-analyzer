const API_URL = import.meta.env.VITE_API_URL;

export async function uploadResume(file) {
    const formData = new FormData();
    formData.append("file", file);

    const response = await fetch(`${API_URL}/upload`, {
        method: "POST",
        body: formData,
    });

    if (!response.ok) {
        throw new Error("Failed to upload resume");
    }

    return response.json();
}

export async function analyzeJobDescription(file, jobDescription) {
    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_description", jobDescription);

    const response = await fetch(`${API_URL}/analyze-jd`, {
        method: "POST",
        body: formData,
    });

    if (!response.ok) {
        throw new Error("Failed to analyze job description");
    }

    return response.json();
}