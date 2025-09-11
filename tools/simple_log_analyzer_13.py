"""
Tool: simple_log_analyzer_13 | Commit #2
Safe cybersecurity tool example: simple_log_analyzer
"""

import os
import hashlib

def simple_log_analyzer(file_path="test.txt"):
    """Example safe function"""
    if not os.path.isfile(file_path):
        return "File does not exist."
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

if __name__ == "__main__":
    print("simple_log_analyzer_13 output:", simple_log_analyzer())

# Unique comment for commit #2
