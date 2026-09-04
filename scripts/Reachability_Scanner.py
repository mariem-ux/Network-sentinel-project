
#!/usr/bin/env python3

import socket

TIMEOUT = 3  # seconds per connection attempt

TESTS = [
    {
        "name"    : "WAN → DMZ Web Server (port forwarding)",
        "host"    : "192.168.1.2",
        "port"    : 80,
        "expect"  : "PASS",   # should succeed (port forward to Ubuntu)
    },
    {
        "name"    : "WAN → LAN PC Host",
        "host"    : "192.168.2.10",
        "port"    : 80,
        "expect"  : "FAIL",   # should be blocked by firewall
    },
    {
        "name"    : "WAN → OPNsense LAN GUI",
        "host"    : "192.168.2.1",
        "port"    : 443,
        "expect"  : "FAIL",   # should be blocked by firewall
    },
]


def check_connection(host, port, timeout):
    """Try to open a TCP connection. Returns True if successful."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception:
        return False


def run_scanner():
    print("=" * 60)
    print("   FIREWALL REACHABILITY SCANNER")
    print("   Running from: Kali VM (WAN — 192.168.1.156)")
    print("=" * 60)

    passed = 0
    failed = 0

    for test in TESTS:
        reachable = check_connection(test["host"], test["port"], TIMEOUT)
        actual    = "PASS" if reachable else "FAIL"
        correct   = actual == test["expect"]

        if correct:
            status = "✔  OK  "
            passed += 1
        else:
            status = "✘ WRONG"
            failed += 1

        print(f"\n  Test : {test['name']}")
        print(f"  Target  : {test['host']}:{test['port']}")
        print(f"  Expected: {test['expect']}  |  Got: {actual}  |  [{status}]")

    print("\n" + "=" * 60)
    print(f"  RESULTS — Passed: {passed}/{len(TESTS)}  |  Failed: {failed}/{len(TESTS)}")

    if failed == 0:
        print("  ✔ All firewall rules are working correctly!")
    else:
        print("  ✘ Some rules need to be checked!")

    print("=" * 60)

if __name__ == "__main__":
    run_scanner()