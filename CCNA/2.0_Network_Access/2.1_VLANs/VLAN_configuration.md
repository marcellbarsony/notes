## VLAN configuration

By default, all ports on a switch are in **VLAN 1**.
This can be verified by typing the `show vlan` command in **enable** mode.

<img src="ttps://www.dropbox.com/s/ejl6shipfxydm7u/vlan1.jpg?dl=1" alt="vlan1_verification" class="inline" />

In the above picture, all of the 24 ports of the switch are in the same VLAN: VLAN1.

Two steps required to create a VLAN and assign a switch port to the VLAN:

1. Create a VLAN in **global mode** using the `vlan <number>` command:

The command (`vlan 2`) created VLAN 2.
We've entered the Fa0/1 subinterface mode and configured the interface as an access interface that belongs to VLAN 2.

2. Assign a port to the VLAN by using two interface subcommands:

- `switchport mode access` - Specify the interface that the interface is an access interface.
- `switchport access vlan <number>` - Assign the interface to a VLAN.

<img src="https://www.dropbox.com/s/praytcoi3f3kql8/vlan2_creation.jpg?dl=1" alt="vlan2_creation" class="inline" />
