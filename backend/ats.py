def calculate_score(resume_skills, jd_skills):

    resume_map = {
        skill.lower(): skill
        for skill in resume_skills
    }

    jd_map = {
        skill.lower(): skill
        for skill in jd_skills
    }

    matched_keys = set(resume_map.keys()) & set(jd_map.keys())
    missing_keys = set(jd_map.keys()) - set(resume_map.keys())

    if len(jd_map) == 0:
        score = 0
    else:
        score = round(
            (len(matched_keys) / len(jd_map)) * 100
        )

    if score >= 80:
        rating = "Excellent"
    elif score >= 60:
        rating = "Good"
    elif score >= 40:
        rating = "Needs Improvement"
    else:
        rating = "Low Match"

    suggestions = []

    suggestion_templates = {
        "sql": "Add SQL experience, database projects, queries, joins, or data management work if applicable.",
        "react": "Highlight React projects, components, hooks, or frontend development experience if applicable.",
        "fastapi": "Mention FastAPI, REST API development, or backend projects if you have relevant experience.",
        "python": "Highlight Python projects, automation, backend development, or data-related work if applicable.",
        "java": "Highlight Java projects, object-oriented programming, or backend development experience if applicable.",
        "javascript": "Highlight JavaScript projects, APIs, or frontend development experience if applicable.",
        "typescript": "Highlight TypeScript projects, typed JavaScript development, or frontend/backend experience if applicable.",
        "git": "Mention Git, GitHub repositories, version control, branching, or collaborative development experience if applicable.",
        "github": "Mention GitHub repositories, open-source contributions, or collaborative development experience if applicable.",
        "docker": "Highlight Docker usage, containerization, Dockerfiles, or deployment experience if applicable.",
        "aws": "Mention relevant AWS services, cloud projects, deployments, or cloud infrastructure experience if applicable.",
        "azure": "Mention Azure services, cloud projects, deployments, or cloud infrastructure experience if applicable.",
        "gcp": "Mention Google Cloud Platform services, cloud projects, deployments, or cloud infrastructure experience if applicable.",
        "mongodb": "Highlight MongoDB projects, collections, queries, or NoSQL database experience if applicable.",
        "mysql": "Highlight MySQL databases, SQL queries, relational database projects, or data management experience if applicable.",
        "postgresql": "Highlight PostgreSQL databases, SQL queries, relational database projects, or backend experience if applicable.",
        "kotlin": "Highlight Kotlin projects, Android development, or Kotlin-based application experience if applicable.",
        "android": "Highlight Android applications, mobile development projects, or Android SDK experience if applicable.",
        "swift": "Highlight Swift projects, iOS development, or mobile application experience if applicable.",
        "ios": "Highlight iOS applications, mobile development projects, or Apple platform experience if applicable.",
        "flutter": "Highlight Flutter applications, Dart development, or cross-platform mobile projects if applicable.",
        "react native": "Highlight React Native applications, mobile development, or cross-platform projects if applicable.",
        "node": "Highlight Node.js projects, backend APIs, or server-side JavaScript experience if applicable.",
        "node.js": "Highlight Node.js projects, backend APIs, or server-side JavaScript experience if applicable.",
        "django": "Highlight Django projects, REST APIs, or Python backend development experience if applicable.",
        "flask": "Highlight Flask projects, REST APIs, or Python backend development experience if applicable.",
        "kubernetes": "Highlight Kubernetes clusters, container orchestration, or cloud deployment experience if applicable.",
        "tensorflow": "Highlight TensorFlow projects, machine learning models, or deep learning experience if applicable.",
        "pytorch": "Highlight PyTorch projects, machine learning models, or deep learning experience if applicable.",
        "machine learning": "Highlight machine learning projects, models, algorithms, or data science experience if applicable.",
        "deep learning": "Highlight deep learning projects, neural networks, or AI model development experience if applicable.",
        "linux": "Mention Linux administration, command-line usage, server management, or development experience if applicable."
    }

    for k in sorted(missing_keys):
        skill = jd_map[k]

        if k in suggestion_templates:
            suggestions.append(suggestion_templates[k])
        else:
            suggestions.append(
                f"Consider adding {skill} to your resume if you have relevant experience."
            )

    return {
        "score": score,
        "rating": rating,
        "matched": sorted(
            [jd_map[k] for k in matched_keys]
        ),
        "missing": sorted(
            [jd_map[k] for k in missing_keys]
        ),
        "suggestions": suggestions
    }