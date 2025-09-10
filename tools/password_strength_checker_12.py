"""
Tool: password_strength_checker_12 | Commit #23
Safe cybersecurity tool example: password_strength_checker
"""

import os
import hashlib

def password_strength_checker(file_path="test.txt"):
    """Example safe function"""
    if not os.path.isfile(file_path):
        return "File does not exist."
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

if __name__ == "__main__":
    print("password_strength_checker_12 output:", password_strength_checker())

# Unique comment for commit #23
