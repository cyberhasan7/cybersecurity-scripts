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
