# Network Sentinel – Cybersecurity Internship Project

A fully functional network security lab built from scratch: from network segmentation
and firewall rules, to launching real attacks, analyzing them at the packet level, and
deploying an active Intrusion Detection/Prevention System (IDS/IPS) with real-time
monitoring.

This project covers the full security lifecycle: **build → attack → analyze → defend → monitor.**

---

## Project Summary

This project was built from scratch : starting with nothing but a hypervisor and a few
virtual machines, and ending with a fully functional network security lab that can
detect, block, and log real attacks in real time.

**Phase 1** focused on building the foundation: a segmented network with three distinct
zones (WAN, LAN, DMZ) separated by an OPNsense firewall with strict access rules. An
Ubuntu web server was deployed in the DMZ, NAT and port forwarding were configured to
expose it externally, and an encrypted VPN tunnel was established for secure remote
administration.

**Phase 2** turned the lab into a security system. Using Kali Linux, three real attacks
were launched against the network: an Nmap port scan, an hping3 SYN flood, and a Hydra
brute-force attack. Each attack was captured in Wireshark and analyzed at the packet
level. Using these findings, Suricata was deployed on the firewall with custom detection
rules targeting the exact attack signatures observed. Once validated, Suricata was
switched to full prevention (IPS) mode, and all three attacks were re-launched — this
time, every malicious packet was dropped before reaching the server. Finally, a Syslog
forwarding pipeline was built so Suricata alerts are sent in real time to a central
monitoring script, simulating a basic SIEM (Security Information and Event Management)
pipeline.

---

## Project Timeline

### Phase 1 – Architecture & Secure Connectivity

- **Sprint 1 – Network Segmentation & Firewall:** WAN/LAN/DMZ segmentation, OPNsense ACLs, NAT/port forwarding to the DMZ web server.
  → [`commands/sprint1_firewall_commands.md`](commands/sprint1_firewall_commands.md)

- **Sprint 2 – Encrypted VPN Tunneling:** WireGuard key generation, tunnel configuration, and remote secure access.
  → [`commands/sprint2_vpn_commands.md`](commands/sprint2_vpn_commands.md)

### Phase 2 – Traffic Analysis & Active Defense

- **Sprint 3 – Attack Simulation & PCAP Analysis:** Nmap, hping3, and Hydra attacks; Wireshark packet analysis.
  → [`commands/sprint3_attack_commands.md`](commands/sprint3_attack_commands.md)

- **Sprint 4 – IDS/IPS with Suricata:** Custom detection rules, transition to prevention mode, real-time Syslog monitoring.
  → [`suricata-rules/custom.rules`](suricata-rules/custom.rules)

---

## Repository Structure

```text
network-sentinel-project/
├── commands/       -> Documented commands used in each sprint
├── docker/         -> Containerized demo environment (attacker, target, Suricata)
├── docs/           -> Project documentation (Limitations & Future Improvements)
├── images/         -> Screenshots and network architecture diagram
├── report/         -> Full written project report (PDF)
├── scripts/        -> Bonus Python/Bash automation scripts
└── suricata-rules/ -> Custom Suricata IDS/IPS detection rules
```

---

## Bonus Automation Scripts

| Script | Purpose |
|---|---|
| `Reachability_Scanner.py` | Automatically tests firewall ACL rules across network zones |
| `VPN_Log_Parser.py` | Monitors WireGuard peer handshakes in real time |
| `PCAP_Analyzer.py` | Parses `.pcap` files and extracts top talking IP addresses |
| `SIEM_Listener.py` | Receives Suricata Syslog alerts and displays them in real time |

---

## Note on the Docker Demo

This containerized environment focuses on **detection (IDS mode)**: the attacker
container generates real traffic, and Suricata inspects it live and logs custom
alerts when malicious patterns are detected , fully reproducible with one command.

**Full prevention (IPS) mode**, where Suricata actively drops malicious packets in
real time, was implemented and validated in the original VM-based lab using
OPNsense + inline Suricata (see `report/` and Sprint 4 screenshots in `images/`).
Replicating full inline IPS across Docker's container networking was intentionally
out of scope for this demo to keep it lightweight and reliable.

---

## Tools & Technologies

- **Firewall:** OPNsense
- **Virtualization:** VirtualBox
- **Attack Tools:** Kali Linux, Nmap, hping3, Hydra
- **Traffic Analysis:** Wireshark, tcpdump
- **IDS/IPS:** Suricata
- **VPN:** WireGuard
- **Automation:** Python

---

## Limitations & Future Improvements

See [`docs/limitations&improvements.md`](docs/limitations&improvements.md) for a full breakdown of current
limitations and planned improvements, including expanded attack coverage, high
availability firewall testing, and integration with a real SIEM platform.

---

## Author

**Mariem Rmili**
Cybersecurity Internship , No Breach Training Hub
