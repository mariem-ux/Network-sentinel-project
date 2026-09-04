--------------------------------------------------------------------------------
SPRINT 2: Encrypted VPN Tunneling
--------------------------------------------------------------------------------

## Kali Key Generation

wg genkey
→ Generates a secure, random WireGuard private key on the Kali Linux client.

wg pubkey
→ Derives the corresponding public key from an existing WireGuard private key.

## Kali Client Configuration

sudo chmod 600 /etc/wireguard/wg0.conf
→ Restricts file permissions so only root can read the VPN config and private key.

## Connecting Kali to the VPN

sudo apt install resolvconf -y
→ Installs the utility required to dynamically manage DNS resolution through the tunnel.

sudo wg-quick up wg0
→ Initializes and activates the WireGuard VPN interface, routing configured subnet traffic through the tunnel.

## Verify the Connection

sudo wg show
→ Displays current WireGuard interface status, peer handshakes, transfer stats, and allowed IP routes.

## Sprint 2 Validation and Testing

curl -k https://192.168.2.1
→ Fetches the OPNsense Web GUI login page over HTTPS from Kali, bypassing SSL validation, over the VPN.

sudo wg-quick down wg0
→ Tears down and deactivates the active WireGuard VPN tunnel.

## Bonus: VPN Monitor Script

python3 /root/vpn_monitor_final.py
→ Runs a Python script on OPNsense that checks every 10 seconds for active WireGuard peer handshakes.
