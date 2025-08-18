#!/usr/bin/env python3
"""
wifi_scanner.py
Tool #9 — Passive Wi-Fi Scanner

- Lists nearby Wi-Fi SSIDs, signal strength, security type, channel, etc.
- Works cross-platform using system commands.
- Defensive / educational only.
"""

import platform
import subprocess
import re
import sys

def run(cmd):
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

# ---------------- Windows ----------------
def scan_windows():
    out = run("netsh wlan show networks mode=bssid")
    networks = []
    current = {}
    for line in out.splitlines():
        line = line.strip()
        if line.startswith("SSID"):
            if current:
                networks.append(current)
                current = {}
            ssid = line.split(":", 1)[1].strip()
            current["SSID"] = ssid
        elif line.startswith("Signal"):
            sig = line.split(":", 1)[1].strip()
            current["Signal"] = sig
        elif line.startswith("Authentication"):
            auth = line.split(":", 1)[1].strip()
            current["Auth"] = auth
    if current:
        networks.append(current)
    return networks

# ---------------- Linux ----------------
def scan_linux():
    out = run("nmcli -f SSID,SIGNAL,SECURITY dev wifi list")
    networks = []
    for line in out.splitlines()[1:]:
        parts = line.split()
        if not parts:
            continue
        ssid = parts[0]
        signal = parts[1] if len(parts) > 1 else "?"
        security = " ".join(parts[2:]) if len(parts) > 2 else "?"
        networks.append({"SSID": ssid, "Signal": signal, "Auth": security})
    return networks

# ---------------- macOS ----------------
def scan_macos():
    # airport binary is usually at this path
    out = run("/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s")
    networks = []
    for line in out.splitlines()[1:]:
        parts = line.split()
        if not parts:
            continue
        ssid = parts[0]
        bssid = parts[1]
        rssi = parts[2]
        channel = parts[3]
        auth = " ".join(parts[4:])
        networks.append({
            "SSID": ssid,
            "BSSID": bssid,
            "Signal": rssi,
            "Channel": channel,
            "Auth": auth
        })
    return networks

# ---------------- Runner ----------------
def main():
    osname = platform.system()
    print(f"OS detected: {osname}")
    if osname == "Windows":
        nets = scan_windows()
    elif osname == "Linux":
        nets = scan_linux()
    elif osname == "Darwin":
        nets = scan_macos()
    else:
        print("Unsupported OS")
        sys.exit(1)

    if not nets:
        print("No networks found (or insufficient privileges).")
        return

    print("\nNearby Wi-Fi Networks:")
    print("-" * 60)
    for n in nets:
        for k, v in n.items():
            print(f"{k}: {v}")
        print("-" * 60)

if __name__ == "__main__":
    main()
