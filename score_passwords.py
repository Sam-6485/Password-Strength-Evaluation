import re

def score_password(password):
    score = 0
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>_\-\+=]", password):
        score += 1
    return score

with open("passwords.txt") as f:
    for line in f:
        pw = line.strip()
        print(f"{pw}: Score {score_password(pw)}/6")
