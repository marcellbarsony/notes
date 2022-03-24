# Port Address Translation (PAT)

**Port Address Translation (PAT)** is an extension of NAT that permits multiple devices on a LAN to be mapped to a single Public IP address to conserve IP addresses.

**PAT** is similar to port forwarding except that an incoming packet with destination port (external port) is translated to a a packet different destination port (an internal port).
The ISP assigns a single IP address to the edge device.
When a computer logs on to the Internet, this device assigns the client a port number that is appended to the internal IP address, giving the computer a unique IP address.

If another computer logs on the Internet, this device assigns it the same Public IP address, but a different port number.
Although both computers are sharing the same Public IP address, this device knows which computer to send its packets, because the device uses the port numbers to assign the packets the unique internal IP address of the computers.

[[Cisco - Port Address Translation](<https://www.cisco.com/assets/sol/sb/RV320_Emulators/RV320_Emulator_v1-1-0-09/help/Setup13.html#:~:text=Port%20Address%20Translation%20(PAT)%20is,address%20to%20conserve%20IP%20addresses.)]

With **PAT**, a single Public IP address is used for all internal Private IP addresses, but a different port is assigned to each Private IP address.
This type of NAT is also known as **NAT Overload** and is the typical form of NAT used in today's networks.

**PAT** works by creating dynamic NAT mapping, in which a global (public) IP address and a unique port number are selected.
The router keeps a NAT table entry for every unique combination of the private IP address and port, with translation to the global address and a unique port number.

## PAT Configuration

To configure **PAT**, the following commands are required:

- Configure the router’s inside interface using the `ip nat inside` command.
- Configure the router’s outside interface using the `ip nat outside` command.
- Configure an access list that includes a list of the inside source addresses that should be translated.
- Enable PAT with the `ip nat inside source list <acl_number> interface <interface> overload` global configuration command.
