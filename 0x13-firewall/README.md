0-block_all_incoming_traffic_but
This script is used to block all incoming traffic but allow specified ports.
It uses the Uncomplicated Firewall (ufw) to configure the firewall rules.

## Usage

1. Run the script with sudo privileges.
2. Before each command is executed, a message will pop up for confirmation.
3. After the script is executed, incoming traffic will be blocked except for
the specified ports.

### Ports allowed:
- 22 (SSH)
- 443 (HTTPS SSL)
- 80 (HTTP)

### Ports blocked:
- All other ports are blocked.
