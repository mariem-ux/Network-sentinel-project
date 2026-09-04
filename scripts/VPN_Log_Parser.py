#!/usr/bin/env python3
import subprocess
import sys
import time

def red(text):    print("\033[91m[!!!] " + text + "\033[0m")
def green(text):  print("\033[92m[+] "   + text + "\033[0m")
def yellow(text): print("\033[93m[~] "   + text + "\033[0m")

def check_handshake():
    result = subprocess.run(
        ["wg", "show", "wg0", "latest-handshakes"],
        capture_output=True, text=True
    )
    return result.stdout

def monitor():
    print("-" * 55)
    green("WireGuard VPN Monitor _ Handshake Checker")
    green("OPNsense Server: 192.168.2.1")
    green("VPN Tunnel: 10.100.0.0/24")
    yellow("Checking every 10 seconds...")
    yellow("Press Ctrl+C to stop")
    print("-" * 55)

    while True:
        try:
            output = check_handshake()

            if not output or output.strip() == "":
                red("NO PEERS CONNECTED")
            else:
                for line in output.splitlines():
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split()
                    if len(parts) >= 2:
                        peer = parts[0][:20] + "..."
                        try:
                            timestamp = int(parts[1])
                            now = int(time.time())
                            age = now - timestamp

                            if timestamp == 0:
                                print()
                                red("NO HANDSHAKE RECORDED - peer has not connected yet")
                                red("Peer : " + peer)
                                print()
                            elif age > 180:
                                print()
                                red("NO HANDSHAKE FOR " + str(age) + "SECONDS - peer offline or unreachable")
                                red("Peer : " + peer)
                                print()
                            else:
                                green("Peer " + peer + " OK , last handshake: " + str(age) + "s ago")

                        except ValueError:
                            yellow("Could not parse timestamp for peer: " + peer)

            time.sleep(10)

        except KeyboardInterrupt:
            print()
            green("Monitor stopped.")
            sys.exit(0)
        except Exception as e:
            red("Error: " + str(e))
            sys.exit(1)

if __name__ == "__main__":
    monitor()