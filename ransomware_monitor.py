# ransomware_monitor.py

import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Folder to monitor (you can change this to any folder you want)
MONITORED_FOLDER = os.path.expanduser("~")  # User home folder

# Suspicious file extensions often used by ransomware
SUSPICIOUS_EXTENSIONS = [".encrypted", ".locked", ".crypt", ".enc"]

class RansomwareHandler(FileSystemEventHandler):
    def on_modified(self, event):
        self.check_suspicious(event.src_path)

    def on_created(self, event):
        self.check_suspicious(event.src_path)

    def on_moved(self, event):
        self.check_suspicious(event.dest_path)

    def check_suspicious(self, path):
        filename = os.path.basename(path).lower()
        for ext in SUSPICIOUS_EXTENSIONS:
            if filename.endswith(ext):
                print(f"⚠️ Suspicious file activity detected: {path}")

def start_monitor():
    print(f"🔍 Monitoring folder for suspicious activity: {MONITORED_FOLDER}")
    event_handler = RansomwareHandler()
    observer = Observer()
    observer.schedule(event_handler, MONITORED_FOLDER, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    start_monitor()
