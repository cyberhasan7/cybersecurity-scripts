import socket
import dns.resolver

def dns_lookup(domain):
    print(f"\n🔍 DNS Lookup for: {domain}\n")
    try:
        # Get IP Address
        ip = socket.gethostbyname(domain)
        print(f"🌐 A Record (IP Address): {ip}")
    except socket.gaierror:
        print("❌ Could not resolve domain.")
        return

    # DNS Record Types to Check
    record_types = ["MX", "NS", "TXT"]

    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"\n📌 {record} Records:")
            for rdata in answers:
                print(f"   - {rdata}")
        except Exception as e:
            print(f"   ❌ No {record} record found.")

if __name__ == "__main__":
    domain = input("🔹 Enter a domain (e.g., example.com): ")
    dns_lookup(domain)
