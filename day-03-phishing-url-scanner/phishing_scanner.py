import re
from urllib.parse import urlparse


KEYWORDS = [
    "login",
    "verify",
    "secure",
    "update",
    "account",
    "bank",
    "paypal"
]


def phish_score(url):
    p = urlparse(url)
    score = 0
    reasons = []

    # Check 1: HTTPS
    if p.scheme != "https":
        score += 30
        reasons.append("URL is not using HTTPS")

    # Check 2: Suspicious keywords
    for kw in KEYWORDS:
        if kw in p.netloc.lower():
            score += 20
            reasons.append(f"Suspicious keyword found: {kw}")

    # Check 3: Too many dots/subdomains
    if p.netloc.count(".") > 3:
        score += 25
        reasons.append(f"Too many subdomains: {p.netloc}")

    # Check 4: IPv4 address
    if re.fullmatch(
        r"\d{1,3}(\.\d{1,3}){3}",
        p.netloc
    ):
        score += 40
        reasons.append(f"Suspicious IP address: {p.netloc}")

    return min(score, 100), reasons


# Test URLs
urls = [
    "https://github.com",
    "http://example.com/login",
    "https://login.example.com",
    "https://verify.example.com/account",
    "https://login.verify.account.example.com",
    "http://192.168.1.10/login",
    "https://example.com",
    "http://example.com/bank",
    "https://secure.example.com",
    "https://example.com/update"
]


# Display results
for url in urls:

    score, reasons = phish_score(url)

    print("=" * 60)
    print(f"URL        : {url}")
    print(f"Risk Score : {score}%")

    if reasons:
        print("\nReasons:")
        for reason in reasons:
            print(f"  - {reason}")
    else:
        print("\nReasons:")
        print("  - No suspicious indicators found")

    print("=" * 60)
    print()
