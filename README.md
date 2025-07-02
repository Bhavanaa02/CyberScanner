# 🔐 CyberScanner

**CyberScanner** is a lightweight Python-based CLI tool for basic vulnerability scanning of a target domain or IP. It helps in identifying open ports, SSL certificate expiry, and missing HTTP security headers — a great tool for beginners in cybersecurity and ethical hacking.

---

## 🛠️ Features

- ✅ Scans **common open ports** (21, 80, 443, etc.)
- ✅ Checks **SSL certificate expiry date**
- ✅ Verifies **important HTTP security headers**:
  - Content-Security-Policy
  - Strict-Transport-Security
  - X-Content-Type-Options
  - X-Frame-Options
  - X-XSS-Protection

---

## 📸 Sample Output

![Scan Output](sample_output/amazon_scan.png)

---

## 🚀 Usage

### 1️⃣ Clone the repo

```bash
git clone https://github.com/Bhavanaa02/CyberScanner.git
cd CyberScanner


### 2️⃣ Install requirements

```bash
pip install -r requirements.txt


### 3️⃣ Run the tool

```bash
python scanner.py example.com

Replace `example.com` with any domain like `amazon.in`, `google.com`, etc.

## 🧠 Built With

- Python 3
- `socket`, `ssl`, and `requests` modules
- Basic CLI interface with `argparse`

---

## 📁 Project Structure

CyberScanner/
├── scanner.py # Main CLI script
├── utils.py # Helper functions (ports, SSL, headers)
├── requirements.txt # Python dependencies
├── sample_output/ # Screenshot of sample scan
└── README.md # Project details

---

## 📄 License

This project is licensed under the **MIT License**.  
Feel free to fork, use, and contribute!

---

## 💼 Author

Made with ❤️ by **Bhavana P V**  
📫 Reach me at: [bhavanavijayan02@gmail.com](mailto:bhavanavijayan02@gmail.com)
