# ShadowScanner
🔎 ShadowScan

A Multi-threaded Python Port Scanner

ShadowScan is a lightweight yet powerful port scanning tool written in Python. It mimics the functionality of tools like Nmap but with a clean, customizable, and multi-threaded design. The scanner helps security researchers, students, and penetration testers quickly identify open ports and services on a target system.

✨ Features

🚀 Multi-threaded scanning for faster results

🎯 Custom port range support (e.g., 1-1000)

🔍 Service detection using standard port mappings

⚡ Responsive CLI with flexible options

🛡 Lightweight & cross-platform (runs anywhere with Python 3)

📦 Installation

git clone https://github.com/yourusername/shadowscan.git

cd shadowscan

python3 shadowscan.py --help

▶️ Usage Examples
# Scan first 1024 ports on scanme.nmap.org
python3 shadowscan.py scanme.nmap.org

# Scan ports 1–5000 with 100 threads
python3 shadowscan.py 192.168.1.10 -p 1-5000 -t 100


Sample Output:

[+] Port 22/tcp OPEN (ssh)
[+] Port 80/tcp OPEN (http)
[+] Port 443/tcp OPEN (https)

[✔] ShadowScan completed.

📌 Roadmap

Planned features for future releases:

🔐 Banner grabbing (service version detection)

📝 Export results to JSON/CSV

🌐 UDP scanning support

🕵️ Stealth mode (half-open SYN scan)
