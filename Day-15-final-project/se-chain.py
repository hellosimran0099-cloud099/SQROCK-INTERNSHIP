# se_chain.py — Social Engineering Chain Simulator
from osint_module import run_osint
from profile_module import build_profile
from phish_module import phish_score
from template_module import training_template
from ir_module import ir_response



MODULES = {
    "osint": "Run passive OSINT on a domain",
    "profile": "Build target profile from public data",
    "phish": "Score a URL for phishing indicators",
    "template": "Generate phishing-awareness training email",
    "ir": "Trigger incident response workflow",
}


def menu():
    print("\n" + "=" * 50)
    print("     SOCIAL ENGINEERING CHAIN SIMULATOR")
    print("=" * 50)
    print("     DEVELOPED BY MUHAMMAD IMRAN FROM PAKISTAN")
    print("\n" + "=" * 50)
    for key, description in MODULES.items():
        print(f"{key:<10} : {description}")

    print("exit       : Exit the simulator")
    print("=" * 50)


def main():
    while True:
        menu()

        choice = input("\nEnter module name: ").strip().lower()

        if choice == "exit":
            print("\nExiting simulator...")
            break

        if choice == "osint":
            run_osint()
        elif choice == "profile":
            build_profile()
        elif choice == "phish":
                url = input("\nEnter URL to analyze: ").strip()
                phish_score(url)
        elif choice == "template":
             training_template()
        elif choice == "ir":
            ir_response()
        elif choice in MODULES:
            print(f"\nSelected module: {choice}")
            print(f"Description: {MODULES[choice]}")
        else:
            print("\nInvalid choice. Please select a valid module.")


if __name__ == "__main__":
    main()
