import datetime
import json


def ir_response():

    print("\n=== INCIDENT RESPONSE MODULE ===")

    incident_type = input("Enter incident type: ").strip().lower()

    severity = input(
        "Enter severity (LOW/MEDIUM/HIGH/CRITICAL): "
    ).strip().upper()

    user = input("Enter affected user/email: ").strip()

    if not incident_type:
        print("Incident type cannot be empty.")
        return

    if not user:
        print("Affected user cannot be empty.")
        return

    if severity not in ("LOW", "MEDIUM", "HIGH", "CRITICAL"):
        print("Invalid severity.")
        return

    incident = {
        "type": incident_type,
        "severity": severity,
        "user": user
    }

    print("\n=== INCIDENT RESPONSE TRIGGERED ===")
    print(f"Time     : {datetime.datetime.now()}")
    print(f"Type     : {incident['type']}")
    print(f"Severity : {incident['severity']}")
    print(f"User     : {incident['user']}")

    actions = []

    if severity in ("HIGH", "CRITICAL"):
        actions += [
            "LOCK user account",
            "Revoke active sessions",
            "Notify SOC team",
            "Preserve mail logs"
        ]

    if incident_type == "phishing":
        actions += [
            "Quarantine email",
            "Block sender domain",
            "Scan attachments in sandbox"
        ]

    if severity == "MEDIUM":
        actions += [
            "Review security logs",
            "Monitor affected account"
        ]

    if severity == "LOW":
        actions += [
            "Record incident",
            "Continue monitoring"
        ]

    print("\n=== ACTIONS TAKEN ===")

    for action in actions:
        print(f"  [x] {action}")

    report = {
        "incident": incident,
        "actions": actions,
        "timestamp": str(datetime.datetime.now())
    }

    with open("ir_report.json", "w") as f:
        json.dump(report, f, indent=2)

    print("\nIR report saved: ir_report.json")
