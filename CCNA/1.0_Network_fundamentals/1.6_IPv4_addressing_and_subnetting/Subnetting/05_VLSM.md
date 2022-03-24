# Variable Length Subnet Mask

In **VLSM** the subnet design uses more than one mask in the same network which means more than one mask is used for different subnets of a single class A, B, C or a network.
It is used to increase the usability of subnets as they can be of variable size.
It is also defined as the process of subnetting of a subnet.

We have a limited number of private IPv4 addresses that can be be used in every organization - as the internet and most organizations are growing, we need a way to eliminate wasting IPv4 addresses.
One of the ways we can maximize the use of private IPv4 addresses in the organization is through subnetting.

With **VLSM**, we can allot the closest required number of IP addresses into a subnetwork in our LAN.
For example, we don't need to use a `/23` subnet mask in all of our subnets.

**VLSM** has the following advantages:

- More efficient use of IP address space
- Fewer route updates
- Topology changes are hidden
- Hierarchical level for better route summarization

[[Study CCNA - Understanding Variable Length Subnet Mask (VLSM)](https://study-ccna.com/variable-length-subnet-mask-vlsm/)]<br>
[[GeeksforGeeks - Introduction of Variable Length Subnet Mask VLSM](https://www.geeksforgeeks.org/introduction-of-variable-length-subnet-mask-vlsm/)]
