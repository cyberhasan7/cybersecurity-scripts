"""
Tool: basic_ransomware_simulator_8 | Commit #1
Safe cybersecurity tool example: basic_ransomware_simulator
"""

import os
import hashlib

def basic_ransomware_simulator(file_path="test.txt"):
    """Example safe function"""
    if not os.path.isfile(file_path):
        return "File does not exist."
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

if __name__ == "__main__":
    print("basic_ransomware_simulator_8 output:", basic_ransomware_simulator())

# Unique comment for commit #1
