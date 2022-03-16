# Dynamic Configuration of IPv4 Link-local Addresses

**Automatic Private IP Addressing (APIPA)** is a feature in operating systems that enables computers to automatically self-configure an IP address and subnet mask when their DHCP server isn’t reachable.

The IP address range for **APIPA** is **169.254.0.1**-**169.254.255.254**, with the subnet mask of **255.255.0.0**.

[[Study CCNA - APIPA (Automatic Private IP Addressing)](https://study-ccna.com/apipa-automatic-private-ip-addressing/)]

When a DHCP client boots up, it looks for a DHCP server in order to obtain network parameters.
If the client can't communicate with the DHCP server, it uses **APIPA** to configure itself with an IP address from the **APIPA** range.
This way, the host will still be able to communicate with other hosts on the local network segment that are also configured for **APIPA**.

<img src="https://www.dropbox.com/s/na2i5kdkskj2suw/apipa.jpg?dl=1" alt="apipa" class="inline" />

The host on the left is configured as DHCP client.
The host boots up and looks for DHCP servers on the network.
However, the DHCP server is down and can't respond to the host.
After some time - depending on the operating system - the client auto-configures itself with an address from the **APIPA** range.

The **APIPA** service checks regularly for the presence of a DHCP service.
The DHCP server replaces the APIPA networking addresses with dynamically assigned addresses, if it detects a DHCP server on the network.

> Note
>
> If your host is using an IP address from the APIPA range, there is usually a problem on the network.
> Check network connectivity of your host and the status of the DHCP server.

## RFC 3927

Automatic Private IP Address (APIPA) - Referred by Microsoft

## IPv6 Link-Local addresses

Link-local IPv6 addresses are not forwarded by the router to other links.
A Link-local IPv6 address mst be assigned to every network interface on which the IPv6 protocol is enabled.
A host can automatically derive its own link-local IP address or the address can be manually configured.

Link-local addresses have a prefix of `**FE80::/10**`.
They are mostly used for aut-address configuration and neighbor discovery.

|       64 bits       |   64 bits    |
| :-----------------: | :----------: |
| FE80:0000:0000:0000 | Interface ID |

[[Study CCNA](https://study-ccna.com/ipv6-link-local-addresses/)]
