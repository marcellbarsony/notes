# Automatic Private IP Addressing (APIPA)

**Automatic Private IP Addressing (APIPA)** is a feature in operation systems (e.g. Windows) that enables computers to automatically self-configure an IP address and subnet mask if their DHCP server is not reachable.

**APIPA**'s IP address range is `169.254.0.1` - `169.254.255.254`, with the subnet mask of `255.255.0.0`.

If the DHCP Client cannot communicate with a DHCP Server, it uses **APIPA** to configure itself with an IP address from the **APIPA** range.
The **APIPA Service** also checks regularly (every 180 seconds) for the presence of a DHCP Server.
