def analyze_dockerfile(path):
    print(f"[*] Parsing Container Directives: {path}\n")

    has_explicit_user = False

    try:
        with open(path, 'r') as file:

            for idx, line in enumerate(file, 1):

                cleaned = line.strip().upper()

                # Check for explicit USER instruction
                if cleaned.startswith("USER"):
                    has_explicit_user = True

                # Check for unpinned latest image tag
                if cleaned.startswith("FROM") and ":LATEST" in cleaned:
                    print(
                        f"[RISK DETECTED] Line {idx}: "
                        "Base image uses unpinned 'latest' tag."
                    )

                # Check for SSH port declaration
                if "EXPOSE 22" in cleaned:
                    print(
                        f"[CRITICAL PROHIBITED] Line {idx}: "
                        "Container declares SSH protocol port 22."
                    )

        # Check if USER instruction is missing
        if not has_explicit_user:
            print(
                "[RISK DETECTED] Non-compliant posture: "
                "Explicit USER instruction is absent "
                "(Implicit Root execution risk)."
            )

    except Exception as error:
        print(f"[ERROR] Unable to analyze Dockerfile: {error}")
analyze_dockerfile("Dockerfile.txt")
