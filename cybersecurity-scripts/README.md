# 🔐 Cybersecurity Scripts Collection

Basic tools built using Python for cybersecurity learning and practice.

## 🔧 Projects

1. **Port Scanner** — Scan open ports on any host (IPv4)
2. More tools coming soon...

## 💡 About

Created by H. Hasan Ali as part of daily GitHub mini project challenge to improve hands-on cybersecurity skills.


## 🔎 Port Scanner (Tool #1)

This tool scans a given IP address for open ports in the range 20 to 1024 using Python's `socket` module.

### ✅ Features:
- Scans ports quickly with timeout settings
- Tells you which ports are open on a system
- Beginner-friendly and customizable

### 📄 File:
`port_scanner.py`

### ⚙️ How to Use:
1. Run the script:
   ```bash
   python port_scanner.py


2. ## 🔐 Password Strength Checker

Checks if a password is strong using these rules:
- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character

📄 File: `password_checker.py`


## 🧮 File Integrity Checker (Tool #3)

This tool checks whether a file has been changed by comparing its current SHA256 hash with the original one.

### 🔐 Features:
- SHA256 hash-based integrity check
- Lightweight and fast
- Helps detect file tampering or corruption

### 📄 File:
`file_integrity_checker.py`

### ⚙️ How to Use:
1. Run the script:
   ```bash
   python file_integrity_checker.py


## 📧 Tool 4: Email Spoof Simulation (Educational Purpose Only)

This tool simulates email spoofing for cybersecurity awareness. It lets users craft a fake email header (From, To, Subject, Body) and saves it as an `.eml` file.

> ⚠️ This tool does NOT send real spoofed emails. It's for learning how attackers manipulate email headers.

### ✅ Features:
- Set custom "From" and "To" addresses
- Customize subject and body
- Outputs `.eml` file to inspect headers

### 🔍 Sample Usage:
```bash
$ python email_spoof_simulator.py
Enter fake sender email: attacker@fake.com
Enter recipient email: victim@example.com
Enter subject: Urgent!
Enter message body: Please reset your password now!


## 🔍 Tool 5: Phishing URL Checker

A simple Python script to analyze URLs for common phishing signs, helping users spot suspicious links before clicking.

### Features:
- Checks if URL uses HTTPS or not
- Detects if domain is an IP address
- Looks for '@' symbol which can hide phishing tricks
- Warns if URL is too long or ends with suspicious TLDs

### Usage:
```bash
$ python phishing_url_checker.py
Enter the URL to check: http://192.168.1.1/login
```

The script prints warnings and a final verdict about the URL’s safety.

> Note: This is a heuristic tool for awareness and is not 100% accurate. Always use multiple tools and stay cautious!

## 🛡️ Tool 6: Keylogger Detector

A Python tool that scans running processes and flags potential keyloggers based on suspicious keywords.

> ⚠️ This is a basic detection method — real antivirus tools use advanced heuristics.

### ✅ Features:
- Works cross-platform (Windows, Linux, macOS)
- Detects suspicious processes by name
- Lightweight and fast



## 🛡️ Tool 7: Ransomware File Monitor

A Python tool that monitors a folder in real-time and alerts users if suspicious file changes are detected. Useful for early detection of ransomware activity.

> ⚠️ Basic monitoring only — not a replacement for antivirus software.

### ✅ Features:
- Monitors file creation, modification, and renaming
- Detects suspicious extensions like `.encrypted`, `.locked`, `.crypt`, `.enc`
- Works cross-platform (Windows, Linux, macOS)
- Lightweight and easy to run

### 🔍 Usage:
```bash
python ransomware_monitor.py
```

### 📌 Example Output:
```
🔍 Monitoring folder for suspicious activity: /home/user
⚠️ Suspicious file activity detected: /home/user/Documents/important_file.encrypted
```


## 📡 Tool 8: Wi-Fi Password Extractor (Local PC)

A Python tool to list saved Wi-Fi networks and their passwords on your Windows PC.

> ⚠️ Use responsibly. Only extract passwords from networks you own or have permission to access.

### ✅ Features:
- Extracts Wi-Fi SSIDs and saved passwords
- Quick and lightweight
- Educational/security awareness tool

### 🔍 Usage:
```bash
python wifi_password_extractor.py


## 📡 Tool 9: Passive Wi-Fi Scanner

Scans nearby Wi-Fi networks and displays useful info like SSID, signal strength, channel, and security.

### ⚠️ Notes
- Works on **Windows, Linux, macOS**
- Uses built-in system commands:
  - `netsh wlan show networks` (Windows)
  - `nmcli dev wifi list` (Linux)
  - `airport -s` (macOS)
- Requires Wi-Fi interface enabled

### Usage
```bash
python wifi_scanner.py


🧹 Tool #10: Malware Hash Checker

This tool generates the SHA256 hash of any file. Security researchers use this hash to check files against malware databases like VirusTotal.

🚀 Usage
python malware_hash_checker.py suspicious.exe


✅ Example Output:

🧹 Malware Hash Checker
📂 File: suspicious.exe
🔑 SHA256: 3f786850e387550fdab836ed7e6dc881de23001b
👉 You can paste this hash in VirusTotal for malware analysis.


### 🔥 Tool #11 – Fake IP Generator & Logger

* Generates random **IPv4** or **IPv6** addresses
* Saves generated IPs into `fake_ips.txt`
* Useful for testing, anonymization, and load testing

### 12. 🔎 DNS Lookup Tool
**File:** `dns_lookup.py`  
This tool performs DNS lookups for a given domain.  
It resolves the domain into an IP address and retrieves DNS records like **A, MX, NS, TXT**.  

#### Usage:
```bash
python dns_lookup.py


### 13. 💻 System Info Collector
**File:** `system_info_collector.py`  
Collects detailed information about the system, including **OS, CPU, RAM, and Disk usage**.  

#### Usage:
```bash
python system_info_collector.py

### 15. 🧯 Firewall Status Checker
**File:** `firewall_status_checker.py`  
Checks whether the **firewall is enabled or disabled** on Windows, Linux, and macOS.  

#### Usage:
```bash
python firewall_status_checker.py
```

### 16. 🌐 Network Traffic Sniffer (Basic)
**File:** `network_sniffer.py`  
Captures raw **network packets** and extracts:  
- Source IP  
- Destination IP  
- Protocol number  

#### Usage:
```bash
sudo python3 network_sniffer.py
``
``````