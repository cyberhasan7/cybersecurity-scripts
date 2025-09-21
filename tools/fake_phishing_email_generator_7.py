"""
Tool: fake_phishing_email_generator_7 | Commit #14
Safe cybersecurity tool example: fake_phishing_email_generator
"""

import os
import hashlib

def fake_phishing_email_generator(file_path="test.txt"):
    """Example safe function"""
    if not os.path.isfile(file_path):
        return "File does not exist."
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

if __name__ == "__main__":
    print("fake_phishing_email_generator_7 output:", fake_phishing_email_generator())

# Unique comment for commit #14
