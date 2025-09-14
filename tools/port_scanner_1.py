"""
Tool: port_scanner_1 | Commit #1
Safe cybersecurity tool example: port_scanner
"""

import os
import hashlib

def port_scanner(file_path="test.txt"):
    """Example safe function"""
    if not os.path.isfile(file_path):
        return "File does not exist."
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

if __name__ == "__main__":
    print("port_scanner_1 output:", port_scanner())

# Unique comment for commit #1
