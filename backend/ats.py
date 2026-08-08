def calculate_score(resume_skills, jd_skills):

    resume_map = {skill.lower(): skill for skill in resume_skills}
    jd_map = {skill.lower(): skill for skill in jd_skills}

    matched_keys = set(resume_map.keys()) & set(jd_map.keys())
    missing_keys = set(jd_map.keys()) - set(resume_map.keys())

    if len(jd_map) == 0:
        score = 0
    else:
        score = round((len(matched_keys) / len(jd_map)) * 100)

    suggestions = []

    for k in missing_keys:
        skill = jd_map[k]

        if skill.lower() == "sql":
            suggestions.append(
                "Add SQL experience, database projects, queries, joins, or data management work if applicable."
            )

        elif skill.lower() == "react":
            suggestions.append(
                "Highlight React projects, components, hooks, or frontend development experience if applicable."
            )

        elif skill.lower() == "fastapi":
            suggestions.append(
                "Mention FastAPI, REST API development, or backend projects if you have relevant experience."
            )

        elif skill.lower() == "python":
            suggestions.append(
                "Highlight Python projects, automation, backend development, or data-related work if applicable."
            )

        elif skill.lower() == "java":
            suggestions.append(
                "Highlight Java projects, object-oriented programming, or backend development experience if applicable."
            )

        else:
            suggestions.append(
                f"Consider adding {skill} to your resume if you have relevant experience."
            )

    return {
        "score": score,
        "matched": [jd_map[k] for k in matched_keys],
        "missing": [jd_map[k] for k in missing_keys],
        "suggestions": suggestions
    }