def generate_smishing_script(company, message_type, trigger):

    script = f"""
=== SMISHING AWARENESS SCRIPT ===

Organization : {company}
Message Type : {message_type}
Trigger      : {trigger}

[SMS SCENARIO]
This is a simulated SMS phishing awareness scenario.

[RED FLAGS]
-> Unexpected links can be dangerous.
-> Urgent messages should be verified.
-> Never enter passwords or OTPs through suspicious links.
-> Use the organization's official website or app.

[TRAINING LESSON]
This scenario demonstrates:
{trigger}
"""

    return script


print(generate_smishing_script(
    "Training Bank",
    "Account Verification",
    "Urgency + Fear"
))
