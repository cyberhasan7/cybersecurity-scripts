import platform
import subprocess

def check_firewall_status():
    print("🧯 Firewall Status Checker")
    print("-" * 40)

    system = platform.system()

    try:
        if system == "Windows":
            result = subprocess.run(
                ["netsh", "advfirewall", "show", "allprofiles"],
                capture_output=True, text=True
            )
            print(result.stdout)

        elif system == "Linux":
            result = subprocess.run(
                ["ufw", "status"],
                capture_output=True, text=True
            )
            print(result.stdout)

        elif system == "Darwin":  # macOS
            result = subprocess.run(
                ["defaults", "read", "/Library/Preferences/com.apple.alf", "globalstate"],
                capture_output=True, text=True
            )
            state = result.stdout.strip()
            if state == "1":
                print("Firewall: 🟢 Enabled")
            else:
                print("Firewall: 🔴 Disabled")

        else:
            print("Unsupported OS for firewall check.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_firewall_status()
