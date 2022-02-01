## Binary rules

Subnetting binary rules

192.168.1.18/24 or 192.168.1.18 - 255.255.255.0

### Network/Subnet address

Fill the host portion of an address with binary 0's

_Example:_<br>
192.168.1.**00000000** = 192.168.1.**0**

### First host

Fill the host portion of an address with binary 0's, except for the last bit which is set to binary 1.

_Example:_<br>
192.168.1.**00000001** = 192.168.1.**1**

### Last host

Fill the host portion of an address with binary 1's, except for the last bit which is set to binary 0.

_Example:_<br>
192.168.1.**11111110** = 192.168.1.**254**

### Broadcast address

Fill the host portion of an address with binary 1's

_Example:_<br>
192.168.1.**11111111** = 192.168.1.**255**
