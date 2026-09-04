def detect_suspicious_link(text):

    suspicious_patterns = [
        "bit.ly",
        "tinyurl",
        "free-money",
        "login",
        "verify-account",
        "claim-prize",
        "password"
    ]

    text = text.lower()

    found_patterns = []

    for pattern in suspicious_patterns:
        if pattern in text:
            found_patterns.append(pattern)

    score = len(found_patterns) * 15

    if score == 0:
        risk = "LOW"
    elif score <= 30:
        risk = "MEDIUM"
    else:
        risk = "HIGH"

    return score, risk, found_patterns