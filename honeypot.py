import socket
from datetime import datetime, timedelta
from collections import defaultdict
import time

HOST = '0.0.0.0'
PORT = 2222
MAX_CONN = 10
BLOCK_TIME = 60
TIME_WINDOW = 30

connection_log = defaultdict(list)
blocked_ips = {}

def log_connection(addr, data):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open("logs/connections.log", "a") as f:
        f.write(f"[{now}] Connection from {addr[0]}:{addr[1]} — Data: {data.strip()}\n")

def is_blocked(ip):
    if ip in blocked_ips:
        if time.time() < blocked_ips[ip]:
            return True
        else:
            del blocked_ips[ip]
    return False

def check_rate_limit(ip):
    now = time.time()
    connection_log[ip] = [t for t in connection_log[ip] if now - t < TIME_WINDOW]
    connection_log[ip].append(now)

    if len(connection_log[ip]) > MAX_CONN:
        blocked_ips[ip] = now + BLOCK_TIME
        print(f"[!] IP {ip} temporarily blocked for {BLOCK_TIME} seconds")
        return False
    return True

def start_honeypot():
    print(f"[+] Honeypot listening on port {PORT}")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            ip = addr[0]

            if is_blocked(ip):
                print(f"[!] Blocked IP tried to connect: {ip}")
                conn.close()
                continue

            if not check_rate_limit(ip):
                conn.close()
                continue

            with conn:
                data = conn.recv(1024).decode("utf-8", errors="ignore")
                log_connection(addr, data)
                conn.sendall(b"Access denied.\n")

if __name__ == "__main__":
    start_honeypot()

