"""
Tool: keylogger_detector_9 | Commit #2
Safe cybersecurity tool example: keylogger_detector
"""

import os
import hashlib

def keylogger_detector(file_path="test.txt"):
    """Example safe function"""
    if not os.path.isfile(file_path):
        return "File does not exist."
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

if __name__ == "__main__":
    print("keylogger_detector_9 output:", keylogger_detector())

# Unique comment for commit #2
