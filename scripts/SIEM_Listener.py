import socket
import datetime

HOST = "0.0.0.0"  
PORT = 514       

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"[*] Listening for Syslog alerts on UDP port {PORT}...")
print("[*] Waiting for Suricata alerts...\n")

while True:
    data, addr = sock.recvfrom(65535)
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = data.decode("utf-8", errors="ignore")
    print(f"[{timestamp}] FROM {addr[0]}:\n{message}\n{'-'*60}")