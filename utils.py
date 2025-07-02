import socket
import ssl
import requests

COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306]

def scan_ports(target):
    for port in COMMON_PORTS:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            sock.connect((target, port))
            print(f"Port {port} is OPEN")
        except:
            pass
        finally:
            sock.close()

def check_ssl(domain):
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
                expiry = cert['notAfter']
                print(f"SSL certificate expires on: {expiry}")
    except Exception as e:
        print(f"SSL check failed: {e}")

def check_http_headers(domain):
    try:
        if not domain.startswith("http"):
            domain = "https://" + domain
        response = requests.get(domain, timeout=5)
        headers = response.headers

        important_headers = [
            "Content-Security-Policy",
            "Strict-Transport-Security",
            "X-Content-Type-Options",
            "X-Frame-Options",
            "X-XSS-Protection"
        ]

        for h in important_headers:
            if h in headers:
                print(f"{h}: ✅ Present")
            else:
                print(f"{h}: ❌ Missing")

    except Exception as e:
        print(f"HTTP header check failed: {e}")
