## Allowed VLANs

By default, all VLANs are allowed across a trunk link on a Cisco switch.
This can be verified using the `show interfaces trunk` command:

```
SW1#show interfaces trunk
Port        Mode         Encapsulation  Status        Native vlan
Fa0/1       on           802.1q         trunking      1

Port        Vlans allowed on trunk
Fa0/1       1-1005

Port        Vlans allowed and active in management domain
Fa0/1       1,5,10

Port        Vlans in spanning tree forwarding state and not pruned
Fa0/1       1,5,10
```

In the output, we can see that all VLANs (1 through 1005) are allowed on the trunk by default.

### Prevent traffic from traversing

The following command can prevent traffic from certain VLANs from traversing a trunk link:

`(config-if)#switchport trunk allowed vlan {add | all | except | remove} vlan-list`

For example, to prevent traffic from VLAN 5 to traverse the trunk link, the following command can be used on both end of the link:

```
SW1(config)#int fa0/1
SW1(config-if)#switchport trunk allowed vlan remove 5
```
