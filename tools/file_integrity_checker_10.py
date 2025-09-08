"""
Tool: file_integrity_checker_10 | Commit #16
Safe cybersecurity tool example: file_integrity_checker
"""

import os
import hashlib

def file_integrity_checker(file_path="test.txt"):
    """Example safe function"""
    if not os.path.isfile(file_path):
        return "File does not exist."
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

if __name__ == "__main__":
    print("file_integrity_checker_10 output:", file_integrity_checker())

# Unique comment for commit #16
