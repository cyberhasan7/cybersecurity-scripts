"""
Tool: process_anomaly_detector_6 | Commit #7
Safe cybersecurity tool example: process_anomaly_detector
"""

import os
import hashlib

def process_anomaly_detector(file_path="test.txt"):
    """Example safe function"""
    if not os.path.isfile(file_path):
        return "File does not exist."
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

if __name__ == "__main__":
    print("process_anomaly_detector_6 output:", process_anomaly_detector())

# Unique comment for commit #7
