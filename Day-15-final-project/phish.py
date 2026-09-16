# phish_module.py
# Phishing URL detection module for cybersecurity training

def phish_score(url):
    score = 0
    reasons = []

    url_lower = url.lower()

    keywords = [
        "login",
        "verify",
        "secure",
        "update",
        "account",
        "bank",
        "paypal"
    ]

    for keyword in keywords:
        if keyword in url_lower:
            score += 10
            reasons.append(f"Suspicious keyword: {keyword}")

    if url.startswith("http://"):
        score += 10
        reasons.append("URL uses HTTP instead of HTTPS")

    if len(url) > 75:
        score += 15
        reasons.append("URL is unusually long")

    if score > 100:
        score = 100

    print("\n=== PHISHING URL ANALYSIS ===")
    print(f"URL   : {url}")
    print(f"Score : {score}%")

    if reasons:
        print("\nReasons:")
        for reason in reasons:
            print(f"- {reason}")
    else:
        print("\nNo obvious phishing indicators detected.")

    return score
