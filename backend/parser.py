import re
def extract_email(text):
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    match = re.search(pattern, text)

    if match:
        return match.group()

    return ""
def extract_phone(text):
    pattern = r"\b\d{10}\b"

    match = re.search(pattern, text)

    if match:
        return match.group()

    return ""
def extract_name(text):

    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if len(line) > 2:
            return line

    return ""
from skills import SKILLS
def extract_skills(text):

    found = []

    lower_text = text.lower()

    for skill in SKILLS:

        if skill.lower() in lower_text:
            found.append(skill)

    return found
def parse_resume(text):

    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
    }
