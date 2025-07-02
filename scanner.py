import argparse
from utils import scan_ports, check_ssl, check_http_headers

def main():
    parser = argparse.ArgumentParser(description="CyberScanner - A basic vulnerability scanner")
    parser.add_argument("target", help="IP address or domain name to scan")
    args = parser.parse_args()

    target = args.target

    print(f"\n--- Starting CyberScanner on: {target} ---\n")

    # Port scanning
    print("[1] Scanning common ports...")
    scan_ports(target)

    # SSL Certificate check
    print("\n[2] Checking SSL certificate expiry...")
    check_ssl(target)

    # HTTP headers
    print("\n[3] Checking HTTP security headers...")
    check_http_headers(target)

    print("\n--- Scan Complete ---")

if __name__ == "__main__":
    main()
