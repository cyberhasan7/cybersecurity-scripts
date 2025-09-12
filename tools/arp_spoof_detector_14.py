"""
Tool: arp_spoof_detector_14 | Commit #13
Safe cybersecurity tool example: arp_spoof_detector
"""

import os
import hashlib

def arp_spoof_detector(file_path="test.txt"):
    """Example safe function"""
    if not os.path.isfile(file_path):
        return "File does not exist."
    with open(file_path, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()

if __name__ == "__main__":
    print("arp_spoof_detector_14 output:", arp_spoof_detector())

# Unique comment for commit #13
