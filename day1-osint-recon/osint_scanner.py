# python liberrays
import socket
import whois
import requests

# DNS + IP
domain = input("plz enter the domain : ")

ip =socket.gethostbyname(domain)

print("\n - - - DNS INFORMATION - - - - ")
print("your domain :" ,domain)
print("your ip is : ",ip)

# who is information
print("\n - - - who is information - - -")
result = whois.whois(domain)

print("Registrar:", result.registrar)
print("Creation Date:", result.creation_date)
print("Expiration Date:", result.expiration_date)
print("Name Servers:", result.name_servers)

# IP Geolocation
# IP Geolocation
print("\n[+] IP Geolocation")

url = f"http://ip-api.com/json/{ip}"
response = requests.get(url, timeout=10)

print("API Status Code:", response.status_code)

data = response.json()

print("Country:", data.get("country"))
print("Region:", data.get("regionName"))
print("City:", data.get("city"))
print("ISP:", data.get("isp"))
print("Organization:", data.get("org"))
