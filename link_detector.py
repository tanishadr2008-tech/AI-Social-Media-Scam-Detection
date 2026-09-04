import re
from urllib.parse import urlparse


def detect_suspicious_link(text):

    score = 0
    patterns_found = []

    text_lower = text.lower()


    # ---------------- SUSPICIOUS WORDS ----------------

    suspicious_words = [
        "urgent",
        "lottery",
        "prize",
        "winner",
        "free money",
        "click here",
        "verify",
        "password",
        "bank details",
        "limited offer"
    ]

    for word in suspicious_words:

        if word in text_lower:

            score += 10
            patterns_found.append(f"Suspicious word: {word}")


    # ---------------- FIND URLS ----------------

    urls = re.findall(
        r"https?://[^\s]+",
        text
    )


    for url in urls:

        parsed_url = urlparse(url)

        domain = parsed_url.netloc.lower()


        # ---------------- URL SHORTENERS ----------------

        shorteners = [
            "bit.ly",
            "tinyurl.com",
            "goo.gl",
            "t.co",
            "is.gd"
        ]

        for shortener in shorteners:

            if shortener in domain:

                score += 20
                patterns_found.append(
                    f"Suspicious URL shortener: {shortener}"
                )


        # ---------------- HTTP CHECK ----------------

        if url.startswith("http://"):

            score += 10

            patterns_found.append(
                "Non-secure HTTP connection"
            )


        # ---------------- IP ADDRESS URL ----------------

        ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

        if re.search(ip_pattern, domain):

            score += 20

            patterns_found.append(
                "URL uses an IP address instead of a domain"
            )


        # ---------------- @ SYMBOL ----------------

        if "@" in url:

            score += 15

            patterns_found.append(
                "URL contains @ symbol"
            )


        # ---------------- SUSPICIOUS URL KEYWORDS ----------------

        suspicious_url_words = [
            "login",
            "verify",
            "account",
            "password",
            "bank",
            "claim",
            "secure",
            "update"
        ]

        for word in suspicious_url_words:

            if word in url.lower():

                score += 10

                patterns_found.append(
                    f"Suspicious URL keyword: {word}"
                )


        # ---------------- TOO MANY SUBDOMAINS ----------------

        domain_parts = domain.split(".")

        if len(domain_parts) > 4:

            score += 15

            patterns_found.append(
                "Too many subdomains in URL"
            )


    # ---------------- LIMIT SCORE ----------------

    score = min(score, 100)


    # ---------------- RISK CLASSIFICATION ----------------

    if score >= 60:

        risk = "HIGH"

    elif score >= 30:

        risk = "MEDIUM"

    else:

        risk = "LOW"


    return score, risk, patterns_found