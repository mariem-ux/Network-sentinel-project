# Limitations and Future Improvements

## Limitations

1. **Everything was tested in a virtual lab, not real hardware**  
   All machines (firewall, attacker, target) were virtual machines (software-simulated computers running on one physical PC). Real networks have things like slower speeds, physical cable issues, and real internet traffic, none of that was tested here.

2. **Only 3 types of attacks were tested**  
   We only simulated Nmap scans (a tool that checks which doors/ports are open on a computer), SYN floods (a fake-connection attack that overloads a server), and Hydra brute-force (a tool that tries many passwords automatically). Our firewall rules (Suricata) were built specifically to catch these 3 attacks, they haven't been tested against smarter or hidden attacks like encrypted malware traffic.

3. **Only one attacker and one target**  
   We used one Kali Linux VM (a hacking-tool VM) attacking one Ubuntu server. Real attacks often come from multiple computers at once (called a DDoS, Distributed Denial of Service, meaning many machines flood one target together). We didn't test that scenario.

4. **No backup firewall (no redundancy)**  
   We only had one firewall running. If it crashes or reboots, the whole network loses protection. In real companies, there's usually a second backup firewall ready to take over automatically (called High Availability or HA), we didn't set this up.

5. **VPN tested with only one user**  
   A VPN (Virtual Private Network, lets you securely connect to a network from outside) was tested with just one remote device. We didn't test what happens with many users connecting at once, or how to safely remove access for a user later (called key revocation).

6. **Logs are just printed on screen, not saved properly**  
   Our bonus scripts just print security alerts in the terminal (the black command-line window). There's no proper storage, search, or dashboard for these alerts, a real company would use a SIEM (Security Information and Event Management, software that collects and organizes all security logs in one place) instead.

7. **No speed/performance testing**  
   We confirmed the firewall blocks attacks, but never measured if turning on IPS (Intrusion Prevention System, the mode where the firewall actively blocks bad traffic instead of just alerting) slows down normal, legitimate traffic.

---

## Future Improvements

1. **Test more advanced attacks**  
   Add tougher, sneakier attacks (like slow attacks that are hard to detect, or hidden/encrypted malicious traffic) to make sure the firewall rules still catch them.

2. **Use a real SIEM tool**  
   Replace the simple alert-printing script with a real log-management tool like Wazuh or the ELK Stack (free, popular tools used by real security teams to collect and analyze logs).

3. **Automate the setup**  
   Use tools like Ansible or Terraform (tools that let you set up entire networks/servers automatically using code, instead of doing it manually by hand) so the whole lab can be rebuilt in minutes.

4. **Add a backup firewall**  
   Set up a second firewall using CARP (a protocol that lets two firewalls work as a backup pair) so the network stays protected even if one firewall fails.

5. **Test with more computers and users**  
   Add more internal machines and more VPN users to make the lab look closer to a real company network.

6. **Add live threat intelligence**  
   Connect the firewall to live "bad IP" lists from the internet (like AbuseIPDB) so it automatically blocks known dangerous addresses, not just the ones we tested manually.

7. **Measure speed impact**  
   Use a tool like iperf3 (a simple network speed-testing tool) to check if the firewall slows down normal traffic when protection is turned on.

8. **Make VPN login stronger**  
   Add multi-factor authentication (MFA, requiring a second proof of identity, like a phone code, not just a password) to make VPN access more secure.