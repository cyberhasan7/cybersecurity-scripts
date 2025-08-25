import platform
import psutil

def system_info():
    print("🔎 System Information Collector")
    print("-" * 40)
    print(f"System     : {platform.system()}")
    print(f"Node Name  : {platform.node()}")
    print(f"Release    : {platform.release()}")
    print(f"Version    : {platform.version()}")
    print(f"Machine    : {platform.machine()}")
    print(f"Processor  : {platform.processor()}")
    print("-" * 40)
    print(f"CPU Cores  : {psutil.cpu_count(logical=True)}")
    print(f"RAM        : {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
    print(f"Disk Usage : {psutil.disk_usage('/').percent}% used")
    print("-" * 40)

if __name__ == "__main__":
    system_info()
