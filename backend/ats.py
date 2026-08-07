def calculate_score(resume_skills, jd_skills):

    resume_map = {skill.lower(): skill for skill in resume_skills}
    jd_map = {skill.lower(): skill for skill in jd_skills}

    matched_keys = set(resume_map.keys()) & set(jd_map.keys())
    missing_keys = set(jd_map.keys()) - set(resume_map.keys())

    if len(jd_map) == 0:
        score = 0
    else:
        score = round((len(matched_keys) / len(jd_map)) * 100)

    return {
        "score": score,
        "matched": [jd_map[k] for k in matched_keys],
        "missing": [jd_map[k] for k in missing_keys]
    }