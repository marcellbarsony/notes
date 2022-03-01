# CIDR

**Classless Inter-Domain Routing (CIDR)** is a method of public IP address assignment.

Before **CIDR**, public IP addresses were assigned based on the class boundaries:

- **Class A** – the classful subnet mask is **/8**. 16,777,216 IP addresses available (2<sup>24</sup>).
- **Class B** – the classful subnet mask is **/16**. 65,536 IP addresses available
- **Class C** – the classful subnet mask is **/24**. 256 IP addresses available.

The number of usable IP addresses can be calculated with the following formula:

**2 ^ host bits – 2**

In this example (190.5.4.16/28), a company got 14 usable IP addresses from the **190.5.4.16 – 190.5.4.32** range.
There are 4 host bits and 2 to the power of 4 minus 2 is 14.
The first and the last address are the network address and the broadcast address, respectively.
All other addresses inside the range could be assigned to Internet hosts.
