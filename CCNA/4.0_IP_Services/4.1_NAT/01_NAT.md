# Network Address Translation

**Network Address Translation (NAT)** is a method of mapping an IP address space into another by modifying network address information in the IP header of packets while they are in transit across a traffic routing device.

As **Network Address Translation** modifies the IP address information in packets, **NAT** implementation may vary in their specific behavior in various addressing cases and their effect on network traffic.

As part of this capability, **NAT** can be configured to advertise only one address for the entire network to the outside world.
This provides additional security by effectively hiding the entire internal network behind that address.
**NAT** offers the dual functions of security and address conservation and is typically implemented in remote-access environments.

[[Wikipedia - Network Address Translation](https://en.wikipedia.org/wiki/Network_address_translation)]
[[Cisco - Network Address Translation (NAT) FAQ](https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/26704-nat-faq-00.html)]

## NAT Types

There are three different types of **NAT**s:

1. **Static NAT**<br>
   When the local address is converted to a public one, this **NAT** chooses the same one.
   This means there will be a consistent public IP address associated with that router or **NAT** device.

2. **Dynamic NAT**<br>
   Instead of choosing the same IP address every time, this **NAT** goes through a pool of public IP addresses.
   This results in the router or NAT device getting a different address each time the router translates the local address to a public address.

3. **PAT**<br>
   **Port Address Translation** is a type of dynamic NAT, but it bands several local IP addresses to a singular public one.
   Organizations that want all their employees’ activity to use a singular IP address use a **PAT**, often under the supervision of a network administrator.

[[Comptia - What is Network Address Translation](https://www.comptia.org/content/guides/what-is-network-address-translation)]

## NAT Security

Additionally, **NAT** can provide security and privacy:<br>
Because **NAT** transfers packets of data from public to private addresses, it also prevents anything else from accessing the private device.
The router sorts the data to ensure everything goes to the right place, making it more difficult for unwanted data to get by.
It’s not foolproof, but it often acts as the first means of defense for your device.
If an organization wants to protect its data, they’ll need to go further than just a **NAT firewall** — they’ll want to hire a cybersecurity professional.

**NAT** also allows you to display a public IP address while on a local network, helping to keep data and user history private.

## Public vs Private IPv4 Addresses

| Class | Private Address Range          | Public Address Range                                            |
| ----- | ------------------------------ | --------------------------------------------------------------- |
| A     | 10.0.0.0 to 10.255.255.255     | 1.0.0.0 to 9.255.255.255 and 11.0.0.0 to 126.255.255.255        |
| B     | 172.16.0.0 to 172.37.255.255   | 128.0.0.0 to 172.15.255.255 and 172.32.0.0 to 191.255.255.255   |
| C     | 192.168.0.0 to 192.168.255.255 | 192.0.0.0 to 192.167.255.255 and 192.169.0.0 to 223.255.255.255 |
