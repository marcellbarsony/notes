# VTP Configuration

When configuring VTP, devices are belong to the **null domain** by default.
To configure VTP, devices are need to be placed in a specific VTP domain.
Only devices within the same **VTP domain** will be updated with VLAN information.
A switch can only be configured in a single **VTP domain** at any given time.

## VTP Modes

- **VTP server mode** (default mode) – a switch using this mode can create, modify and delete VLANs.
  A VTP server switch will propagate VLAN changes to the same VTP domain.
- **VTP client mode** – VTP clients behave the same way as VTP servers, byt cannot create, change or delete VLANs on a VTP client.
  Received VTP updates are processed and forwarded.
- **VTP transparent mode** – a switch using this mode doesn’t share its VLAN database, but it forwards received VTP advertisements.
  VLANs can be created on a VTP transparent switch, but these changes will not be sent to other switches.
- **VTP mode off** – similar to VTP transparent mode, with a difference that a switch using this mode will not forward received VTP updates.
  This command is supported only in VTP V3.

## VTP Revision Number

The **VTP configuration revision number** is a 32-bit number that indicates the level of revision for a VTP packet.
Each VTP device track the VTP configuration revision number that is assigned to it.
Most of the VTP packets contain the VTP configuration revision number of the sender.

**VTP revision number** is used in order to determine whether the received information is more recent than the current version.
Each time that a VLAN change is made in a VTP device, the configuration revision is incremented by one.
To reset the configuration number of a switch, change the VTP domain name, and then change the name back to the original name.

```
switch(config)#do show vtp status
```

## VTP Password

If a password is configured for VTP, the password must be configured on all switches in the VTP domain - the password must be the same on all switches.
The VTP password is translated by algorithm into a 16-byte word (MD5 value) that is carried in all summary-advertisement VTP packets.

## VTP Pruning

VTP ensures that all switches in the VTP domain are aware of all VLANs.
However, VTP can create unnecessary traffic.
All unknown unicasts and broadcasts in a VLAN are flooded over the entire VLAN.
All switches in a network receive all broadcasts, even in situations in which few users are connected in that VLAN.
**VTP pruning** is a feature that can eliminate or _prune_ unnecessary traffic.

## Commands

| Command                                   | Description                    |
| ----------------------------------------- | ------------------------------ |
| show vlan                                 | Show VLAN database             |
| SW1(config)#vlan 10                       | Create VLAN 10                 |
| SW1(config-if)#switchport mode ?          | Switch port mode               |
| SW1(config-if)#switchport access vlan 100 | Assign port to VLAN            |
| SW1(config)#ip routing                    | Enable IP routing              |
| show vtp status                           | Show VTP status                |
| SW1#show int g0/1 switchport              | Show switch port configuration |

Verify native VLAN configuration

```
Switch1# show int trunk
```

```
Switch1#(config-if)# switchport trunk native vlan 33
```

Set interface port as trunk

```
Switch1(config-if)# switchport trunk encapsulation dot1q
Switch1(config-if)# switchport mode trunk
```
