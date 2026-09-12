def generate_awareness_email(target, scenario):

    if scenario == "IT":
        subject = "Security Awareness Training - Login Alert"
        message = f"""
Hi {target['name']},

This is a simulated security-awareness email
for our authorized laboratory exercise.

A login alert was detected for your account.

[LAB AWARENESS LINK]

Remember:
Never enter your password through an unexpected email link.
Always verify through official IT channels.
"""

    elif scenario == "BANK":
        subject = "Security Awareness Training - Account Alert"
        message = f"""
Hi {target['name']},

This is a simulated bank-security awareness exercise.

A suspicious account activity alert has been generated
for this training scenario.

[LAB AWARENESS LINK]

Remember:
Never provide your password, PIN, or OTP through an email.
Contact your bank using its official contact information.
"""

    elif scenario == "GOV":
        subject = "Security Awareness Training - Account Notice"
        message = f"""
Hi {target['name']},

This is a simulated government-security awareness exercise.

An account verification notice has been generated
for this training scenario.

[LAB AWARENESS LINK]

Remember:
Verify government-related messages through official channels.
Do not provide passwords or sensitive information by email.
"""

    else:
        return "Invalid scenario."

    return f"""
========================================
SECURITY AWARENESS TRAINING EMAIL
========================================
To      : {target['email']}
Company : {target['company']}
Location: {target['location']}
Subject : {subject}

{message}

Regards,
Security Awareness Team
========================================
"""


target = {
    "name": "Ali Khan",
    "email": "ali@lab.example",
    "company": "Cyber Lab",
    "location": "Multan, Pakistan"
}


print(generate_awareness_email(target, "GOV"))
