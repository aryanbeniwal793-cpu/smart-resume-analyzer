def calculate_score(resume_skills, jd_skills):

    resume_map = {skill.lower(): skill for skill in resume_skills}
    jd_map = {skill.lower(): skill for skill in jd_skills}

    matched_keys = set(resume_map.keys()) & set(jd_map.keys())
    missing_keys = set(jd_map.keys()) - set(resume_map.keys())

    if len(jd_map) == 0:
        score = 0
    else:
        score = round((len(matched_keys) / len(jd_map)) * 100)

    # Score interpretation
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
        "git": "Mention Git, GitHub repositories, version control, branching, or collaborative development experience if applicable.",
        "docker": "Highlight Docker usage, containerization, Dockerfiles, or deployment experience if applicable.",
        "aws": "Mention relevant AWS services, cloud projects, deployments, or cloud infrastructure experience if applicable.",
        "mongodb": "Highlight MongoDB projects, collections, queries, or NoSQL database experience if applicable."
    }

    for k in missing_keys:
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
        "matched": sorted([jd_map[k] for k in matched_keys]),
        "missing": sorted([jd_map[k] for k in missing_keys]),
        "suggestions": suggestions
    }