## VLAN configuration

By default, all ports on a switch are in **VLAN 1**.
This can be verified by typing the `show vlan` command in **enable** mode.

Two steps required to create a VLAN and assign a switch port to the VLAN:

1. Create a VLAN in **global mode** using the `vlan <number>` command.

The command (`vlan 2`) created VLAN 2.
We've entered the Fa0/1 subinterface mode and configured the interface as an access interface that belongs to VLAN 2.
To verify this, we can again use the `show vlan` command.

<img src="" alt="" class="inline" />

2. Assign a port to the VLAN by using two interface subcommands:

- `switchport mode access` - Specify the interface that the interface is an access interface.
- `switchport access vlan <number>` - Assign the interface to a VLAN.

Example

<img src="" alt="" class="inline" />
