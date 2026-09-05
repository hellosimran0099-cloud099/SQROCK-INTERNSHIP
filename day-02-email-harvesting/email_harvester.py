import requests
import re

url = input("Enter authorized website URL: ")

try:
    # Website se HTML retrieve
    response = requests.get(url, timeout=10)

    print("\nStatus Code:", response.status_code)

    # HTML content
    html = response.text

    # Email pattern search
    emails = re.findall(
        r'[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}',
        html
    )

    # Duplicate emails remove
    emails = sorted(set(emails))

    print("\n--- EMAIL HARVESTING RESULTS ---")

    if emails:
        for email in emails:
            print(email)
    else:
        print("No email addresses found.")

except requests.RequestException as error:
    print("Request failed:", error)
