--------------------------------------------------------------------------------
SPRINT 1: Network Segmentation and Firewall Configuration
--------------------------------------------------------------------------------

## IP Address Configuration (WAN, LAN, and DMZ)

ifconfig em1
→ Displays and verifies the configuration, active status, IP address, and netmask of the WAN interface on OPNsense.

## Ubuntu Server Installation & Configuring

ip a
→ Displays all active network interface details and verifies the static IP address assigned to the Ubuntu DMZ server.

## Launching the Python Web Server

sudo python3 -m http.server 80
→ Starts a lightweight HTTP web server listening on port 80 across all interfaces on the Ubuntu target.

## Test 1: Web Server Accessibility from Kali Linux (WAN Side)

curl http://192.168.1.2
→ Sends an HTTP GET request from Kali Linux to the OPNsense WAN IP to test NAT port forwarding to the DMZ web server.

## Test 2: DMZ-to-LAN Isolation Verification

ping 192.168.2.10
→ Sends ICMP echo requests from the DMZ server to the LAN host to verify that the firewall blocks DMZ-to-LAN traffic.

## Bonus: Python-Based Reachability Scanner

python3 reachability_scanner.py
→ Executes a custom Python script on Kali to automatically test and validate all firewall access control rules across zones.