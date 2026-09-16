def training_template():

    print("\n=== SECURITY AWARENESS EMAIL MODULE ===")

    name = input("Enter target name: ").strip()
    company = input("Enter company: ").strip()
    location = input("Enter location: ").strip()
    email = input("Enter target email: ").strip()
    link = input("Enter target email: ").strip()

    print("\nSelect Scenario:")
    print("1. IT")
    print("2. GOV")
    print("3. BANK")

    choice = input("Enter choice (1-3): ").strip()

    if choice == "1":
        scenario = "IT"
        subject = "Security Awareness Training - Login Alert"

        message = f"""
Hi {name},

This is a simulated IT security-awareness exercise.

A login alert was detected for your account.

{link}

Remember:
- Never enter your password through an unexpected email.
- Verify login alerts through official IT channels.
- Report suspicious emails to the security team.
"""

    elif choice == "2":
        scenario = "GOV"
        subject = "Security Awareness Training - Account Notice"

        message = f"""
Hi {name},

This is a simulated government-security awareness exercise.

An account verification notice has been generated
for this training scenario.

{link}

Remember:
- Verify government messages through official channels.
- Never provide passwords or sensitive information by email.
- Report suspicious messages to the security team.
"""

    elif choice == "3":
        scenario = "BANK"
        subject = "Security Awareness Training - Account Alert"

        message = f"""
Hi {name},

This is a simulated bank-security awareness exercise.

A suspicious account activity alert has been generated
for this training scenario.

{link}

Remember:
- Never provide your password, PIN, or OTP through email.
- Do not click unexpected banking links.
- Contact your bank using official contact information.
"""

    else:
        print("Invalid scenario. Please select 1, 2, or 3.")
        return

    print(f"""
========================================
SECURITY AWARENESS TRAINING EMAIL
========================================
To       : {email}
Company  : {company}
Location : {location}
Scenario : {scenario}
Subject  : {subject}


{message}

Regards,
Security Awareness Team
========================================
""")
