# wifi_password_extractor.py (fixed version)

import subprocess

def get_saved_wifi_passwords():
    print("🔍 Extracting saved Wi-Fi passwords on this PC...\n")

    try:
        # Use encoding="utf-8" to handle special characters
        result = subprocess.run(
            ["netsh", "wlan", "show", "profiles"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="ignore"  # Ignore characters that can't decode
        )
    except Exception as e:
        print(f"❌ Failed to run netsh: {e}")
        return

    if not result.stdout:
        print("⚠️ No output from netsh command. Are you running on Windows?")
        return

    profiles = [line.split(":")[1].strip() for line in result.stdout.splitlines() if "All User Profile" in line]

    if not profiles:
        print("⚠️ No saved Wi-Fi networks found.")
        return

    for profile in profiles:
        try:
            password_result = subprocess.run(
                ["netsh", "wlan", "show", "profile", profile, "key=clear"],
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="ignore"
            )
            if password_result.stdout:
                password_lines = [line for line in password_result.stdout.splitlines() if "Key Content" in line]
                password = password_lines[0].split(":")[1].strip() if password_lines else "<No password found>"
                print(f"📶 {profile} -> Password: {password}")
            else:
                print(f"📶 {profile} -> <Could not retrieve output>")
        except Exception as e:
            print(f"❌ Could not retrieve password for {profile}: {e}")

if __name__ == "__main__":
    get_saved_wifi_passwords()
