import pyshark
from collections import Counter

cap = pyshark.FileCapture('attacks.pcap')

ip_counter = Counter()

for pkt in cap:
    try:
        ip_counter[pkt.ip.src] += 1
    except AttributeError:
        pass

cap.close()

print("Top 5 IP addresses:\n")
for ip, count in ip_counter.most_common(5):
    print(f"  {ip} — {count} packets")