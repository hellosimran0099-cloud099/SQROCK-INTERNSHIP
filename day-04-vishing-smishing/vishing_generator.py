def generate_vishing_script(target_company, attacker_role, pretext):
    script = f"""
=== VISHING AWARENESS SCRIPT ===
Caller Role : {attacker_role}
Target Org  : {target_company}
Pretext     : {pretext}

[OPENER]
'Hi, this is Alex from IT Support at {target_company}.
We detected unusual activity on your account.'

[HOOK]
'I need to verify your identity — can you confirm
your employee ID and current password?'

[RED FLAG for Awareness]
-> Legitimate IT will NEVER ask for passwords.
-> Always verify via official internal channels.
"""
    return script


# ==========================================
# TRIGGER ANALYZER
# ==========================================

def analyze_trigger(script):

    print("\n=== PSYCHOLOGICAL TRIGGER ANALYSIS ===")

    # Script ko lowercase mein convert karte hain
    text = script.lower()

    detected = False

    # -------------------------
    # AUTHORITY
    # -------------------------
    authority_words = [
        "it support",
        "manager",
        "administrator",
        "official",
        "security team",
        "bank",
        "support"
    ]

    if any(word in text for word in authority_words):
        print("\n[✓] Authority")
        print("    Reason: Script mein official role/authority ka impression detected.")
        detected = True
    else:
        print("\n[ ] Authority")
        print("    Reason: Authority-related indication nahi mila.")

    # -------------------------
    # FEAR
    # -------------------------
    fear_words = [
        "unusual activity",
        "suspicious activity",
        "security problem",
        "account problem",
        "risk",
        "danger",
        "loss"
    ]

    if any(word in text for word in fear_words):
        print("\n[✓] Fear")
        print("    Reason: Script mein possible problem ya security concern create kiya gaya.")
        detected = True
    else:
        print("\n[ ] Fear")
        print("    Reason: Fear-related indication nahi mila.")

    # -------------------------
    # SCARCITY / URGENCY
    # -------------------------
    urgency_words = [
        "immediately",
        "urgent",
        "right now",
        "within minutes",
        "limited time",
        "act now"
    ]

    if any(word in text for word in urgency_words):
        print("\n[✓] Urgency / Scarcity")
        print("    Reason: Script mein time pressure create karne wali language detected.")
        detected = True
    else:
        print("\n[ ] Urgency / Scarcity")
        print("    Reason: Time pressure detect nahi hua.")

    # -------------------------
    # LIKING / TRUST
    # -------------------------
    liking_words = [
        "hi",
        "hello",
        "help",
        "support",
        "friend",
        "assist"
    ]

    if any(word in text for word in liking_words):
        print("\n[✓] Liking / Trust")
        print("    Reason: Friendly/supportive language se trust build karne ki koshish detected.")
        detected = True
    else:
        print("\n[ ] Liking / Trust")
        print("    Reason: Friendly trust-building language nahi mili.")

    # -------------------------
    # CREDENTIAL REQUEST
    # -------------------------
    credential_words = [
        "password",
        "employee id",
        "verification code",
        "otp",
        "pin"
    ]

    if any(word in text for word in credential_words):
        print("\n[!] Credential Request")
        print("    Awareness Red Flag: Sensitive information request detected.")
        detected = True

    # -------------------------
    # FINAL RESULT
    # -------------------------

    print("\n================================")
    print("FINAL ANALYSIS")
    print("================================")

    if detected:
        print("Psychological/social-engineering indicators detected.")
    else:
        print("No known indicators detected.")

    print("\nAwareness Reminder:")
    print("Never share passwords, OTPs, PINs, or other sensitive credentials.")
    print("Verify suspicious requests through an official channel.")


# ==========================================
# MAIN PROGRAM
# ==========================================

generated_script = generate_vishing_script(
    "BOP",
    "Customer Support",
    "transaction activity"
)

# Pehle generated script show karo
print(generated_script)

# Ab SAME generated script analyzer ko do
analyze_trigger(generated_script)
