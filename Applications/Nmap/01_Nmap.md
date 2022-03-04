# Nmap

**Nmap** (**Network Mapper**) is a network scanner created by Gordon Lyon (also known by his pseudonym Fyodor Vaskovich).
**Nmap** is used to discover hosts and services on a computer network by sending packets and analyzing the responses.

[[Nmap](https://nmap.org/)]

## Features

Nmap features include:

- **Host discovery** – Identifying hosts on a network. For example, listing the hosts that respond to TCP and/or ICMP requests or have a particular port open.
- **Port scanning** – Enumerating the open ports on target hosts.
- **Version detection** – Interrogating network services on remote devices to determine application name and version number.
- **TCP/IP stack fingerprinting** – Determining the operating system and hardware characteristics of network devices based on observations of network activity of said devices.
- **Scriptable interaction with the target** – using Nmap Scripting Engine(NSE) and Lua programming language.

Nmap can provide further information on targets, including reverse DNS names, device types, and MAC addresses.

Typical use cases:

- Auditing the security of a device or firewall by identifying the network connections which can be made to, or through it.
- Identifying open ports on a target host in preparation for auditing.
- Network inventory, network mapping, maintenance and asset management.
- Auditing the security of a network by identifying new servers.
- Generating traffic to hosts on a network, response analysis and response time measurement.
- Finding and exploiting vulnerabilities in a network.
- DNS queries and subdomain search