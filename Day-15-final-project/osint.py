# osint_module.py
# Passive OSINT module for training purposes
import whois, socket, requests
def run_osint():
    print("\n=== PASSIVE OSINT MODULE ===")
    
    domain = input("Enter domain: ").strip()
    w = whois.whois(domain)
    ip = socket.gethostbyname(domain)
    geo = requests.get(f"http://ip-api.com/json/{ip}").json()
    print(f"Registrar : {w.registrar}")
    print(f"IP        : {ip}")
    print(f"Location  : {geo['city']}, {geo['country']}")
