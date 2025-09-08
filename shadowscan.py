#!/usr/bin/env python3
import socket
import argparse
import threading
from queue import Queue

# Banner
print(r"""
   _____ _               _          _____                                 
  / ____| |             | |        / ____|                                
 | (___ | |__   __ _  __| | _____ | (___   ___ __ _ _ __  _ __   ___ _ __ 
  \___ \| '_ \ / _` |/ _` |/ _ \ \ \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
  ____) | | | | (_| | (_| |  __/  ____) | (_| (_| | | | | | | |  __/ |   
 |_____/|_| |_|\__,_|\__,_|\___| |_____/ \___\__,_|_| |_|_| |_|\___|_|   

                        ~ ShadowScan v1.0 ~
""")

# Thread worker
def port_scan_worker():
    while not q.empty():
        port = q.get()
        scan_port(port)
        q.task_done()

# Scan single port
def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"
            print(f"[+] Port {port}/tcp OPEN ({service})")
        sock.close()
    except Exception:
        pass

# CLI arguments
parser = argparse.ArgumentParser(description="ShadowScan - Multi-threaded Port Scanner")
parser.add_argument("host", help="Target host (IP or domain)")
parser.add_argument("-p", "--ports", help="Port range (e.g. 1-1000)", default="1-1024")
parser.add_argument("-t", "--threads", help="Number of threads (default=50)", type=int, default=50)
args = parser.parse_args()

target = args.host
start_port, end_port = map(int, args.ports.split("-"))
threads = args.threads

print(f"[~] Scanning {target} from port {start_port} to {end_port} with {threads} threads\n")

# Queue ports
q = Queue()
for port in range(start_port, end_port + 1):
    q.put(port)

# Start threads
for i in range(threads):
    t = threading.Thread(target=port_scan_worker)
    t.daemon = True
    t.start()

q.join()
print("\n[✔] ShadowScan completed.")
