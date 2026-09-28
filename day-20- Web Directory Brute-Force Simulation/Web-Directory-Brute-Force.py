import requests
def audit_directory_paths(base_url, wordlist):
    print(f"[*] Discovering endpoints for: {base_url}")
    for directory in wordlist:
        target_path = f"{base_url}/{directory}"
        try:
            response = requests.get(target_path, timeout=3)
            if response.status_code == 200:
                print(f"[MATCH DETECTED] Route accessible: {target_path} (Status: 200)")
            elif response.status_code == 403:
                print(f"[RESTRICED ROUTE] Forbidden resource mapped: {target_path} (Status: 403)")
            elif response.status_code == 404:
                print(f"[Rote NOT FOUND] : {target_path} (Status: 404)")
        except requests.RequestException:
            pass
audit_directory_paths("http://localhost:5000", ["admin", "dashboard", "api/v1","rendom", 
".env", "backup.sql"])
