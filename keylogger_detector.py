# keylogger_detector.py
# Updated on 2025-08-10 for testing GitHub contribution
 
import psutil

# List of suspicious keywords often used in keylogger process names
SUSPICIOUS_KEYWORDS = [
    "keylogger", "spy", "capture", "logger", "keyboard"
]

def detect_keyloggers():
    print("🔍 Scanning for potential keyloggers...")
    found_suspicious = False

    for proc in psutil.process_iter(['pid', 'name']):
        try:
            process_name = proc.info['name'].lower()
            for keyword in SUSPICIOUS_KEYWORDS:
                if keyword in process_name:
                    print(f"⚠️ Suspicious process detected: {proc.info['name']} (PID: {proc.info['pid']})")
                    found_suspicious = True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    if not found_suspicious:
        print("✅ No suspicious keylogger processes found.")

if __name__ == "__main__":
    detect_keyloggers()
