# Dynamic NAT

**Dynamic NAT** is a many-to-one mapping of a Private IP address or subnets inside the SD-WAN network to a Public IP address or subnet outside the SD-WAN network.
The traffic form different zones and subnets over trusted (inside) IP addresses in the LAN segment is sent over a single Public (outside) IP address.

The router dynamically picks an address from the global address pool that is not currently assigned.
The dynamic entry stays in the NAT Translations table as long as the traffic is exchanged.
The entry time out after a period of inactivity and the global IP address can be used for new translations.

## Dynamic NAT Types

**Dynamic NAT** does Port Address Translation (PAT) along with IP address translation.
Port numbers are used to distinguish which traffic belongs to which IP address.
A single Public IP address is used for all internal Private IP addresses, but a different port number is assigned to each Private IP address.
PAT is a cost effective way to allow multiple hosts to connect to the Internet using a single Public IP address.

- **Port Restricted** — Port Restricted NAT uses the same Outside port for all translations related to an Inside IP address and port pair.
  This mode is typically used to allow internet P2P applications.

- **Symmetric** — Symmetric NAT uses the same Outside port for all translations related to an Inside IP address, Inside port, Outside IP address and Outside Port.
  This mode is typically used to enhance security or expand the maximum number of NAT sessions.

## Inbound and Outbound NAT

The direction for a connection can either be inside-to-outside or outside-to-inside.
When a NAT rule is created, it is applied to both the directions depending on the direction match type.

- **Outbound** — The destination address is translated for packets received on the service.
  The source address is translated for packets transmitted on the service.
  Outbound Dynamic NAT is supported on Local, Internet, Intranet, and Inter-routing domain services.
  For WAN services (such as Internet and Intranet services) the configure WAN link IP address is dynamically chosen as the outside IP address.
  For Local and Inter-routing domain services, provide an outside IP address.
  The Outside zone is derived from the selected device.
  A typical use case of Outbound Dynamic NAT is to simultaneously allow multiple users in your LAN to securely access the internet using a single Public IP address.

- **Inbound** — The source address is translated for packets received on the service.
  The destination address is translated for packets transmitted on the service.
  Inbound Dynamic NAT is not supported on WAN services such as Internet or Intranet.
  There is an explicit audit error to indicate the same.
  Inbound Dynamic NAT is supported on Local and Inter-routing domain services only.
  Provide an outside zone and outside IP address to be translated to.
  A typical use case for inbound dynamic NAT is to allow external users access e-mail or web servers hosted in your private network.

## Dynamic NAT Configuration

With **Dynamic NAT**, the following addresses need to be specified on a Cisco router:

- Inside addresses that will be translated
- Pool of global addresses

To configure **Dynamic NAT**, the following steps are required:

1. Configure the **router’s inside interface** using the `ip nat inside` command
2. Configure the **router’s outside interface** using the `ip nat outside` command
3. Configure an **ACL** that has a list of the inside source addresses that will be translated
4. Configure a **pool of global IP addresses** using the `ip nat pool <name> <first_ip> <last_ip> netmask <subnet_mask>` command
5. Enable **Dynamic NAT** with the `ip nat inside source list <acl_number> pool <name>` global configuration command
