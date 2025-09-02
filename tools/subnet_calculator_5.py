"""
Tool: subnet_calculator_5 | Commit #3
Safe cybersecurity tool example: subnet_calculator
"""

import os
import hashlib

def subnet_calculator(file_path="test.txt"):
    """Example safe function"""
    if not os.path.isfile(file_path):
        return "File does not exist."
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

if __name__ == "__main__":
    print("subnet_calculator_5 output:", subnet_calculator())

# Unique comment for commit #3
