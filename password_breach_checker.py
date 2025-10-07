#!/usr/bin/env python3
"""
Tool #14 - Password Breach Checker
Checks if your password has been exposed in known data breaches.
Uses the HaveIBeenPwned API (safe - no plain password sent).
"""

import hashlib
import requests

def check_password_breach(password):
    # Hash the password using SHA-1
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix = sha1_password[:5]
    suffix = sha1_password[5:]

    # Query the HIBP API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code != 200:
        print("⚠️ Error contacting the API.")
        return

    # Check if the suffix appears in the response
    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            print(f"❌ Password found in data breach! (Seen {count} times)")
            return

    print("✅ Password not found in known breaches. You’re safe!")

if __name__ == "__main__":
    password = input("Enter your password to check: ")
    check_password_breach(password)
    
````````````