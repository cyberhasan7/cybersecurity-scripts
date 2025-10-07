# phishing_url_checker.py

from urllib.parse import urlparse

def is_suspicious_url(url):
    parsed = urlparse(url)

    # Check if scheme is http instead of https
    if parsed.scheme != "https":
        print("⚠️ Warning: URL is not secure (not HTTPS).")

    # Check if URL uses IP address instead of domain
    if parsed.hostname:
        parts = parsed.hostname.split('.')
        if all(part.isdigit() for part in parts if part):
            print("⚠️ Warning: URL uses IP address as domain.")

    # Check for '@' symbol in URL
    if '@' in url:
        print("⚠️ Warning: URL contains '@' symbol which can be used for phishing.")

    # Check for suspicious length
    if len(url) > 75:
        print("⚠️ Warning: URL is unusually long.")

    # Check for multiple dots or suspicious TLDs (example: .xyz, .top)
    suspicious_tlds = ['.xyz', '.top', '.club', '.info', '.biz']
    if any(url.endswith(tld) for tld in suspicious_tlds):
        print("⚠️ Warning: URL ends with suspicious top-level domain.")

    # Simple heuristic conclusion
    warnings = [
        parsed.scheme != "https",
        parsed.hostname and all(part.isdigit() for part in parsed.hostname.split('.') if part),
        '@' in url,
        len(url) > 75,
        any(url.endswith(tld) for tld in suspicious_tlds)
    ]

    if any(warnings):
        print("\n🚨 This URL is potentially phishing or suspicious. Be careful!")
    else:
        print("\n✅ This URL looks safe — but always stay alert!")

if __name__ == "__main__":
    print("🔍 Phishing URL Checker")
    url_input = input("Enter the URL to check: ").strip()
    is_suspicious_url(url_input)
