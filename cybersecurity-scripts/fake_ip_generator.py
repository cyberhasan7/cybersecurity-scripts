import random

def generate_ipv4():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

def generate_ipv6():
    return ":".join("{:x}".format(random.randint(0, 65535)) for _ in range(8))

def main():
    print("🌐 Fake IP Generator Tool 🌐")
    count = int(input("How many fake IPs you want? "))
    ip_type = input("Choose type (ipv4/ipv6): ").strip().lower()

    with open("fake_ips.txt", "w") as f:
        for _ in range(count):
            if ip_type == "ipv6":
                ip = generate_ipv6()
            else:
                ip = generate_ipv4()
            print(ip)
            f.write(ip + "\n")

    print(f"\n✅ {count} fake {ip_type.upper()} addresses saved in fake_ips.txt")

if __name__ == "__main__":
    main()
