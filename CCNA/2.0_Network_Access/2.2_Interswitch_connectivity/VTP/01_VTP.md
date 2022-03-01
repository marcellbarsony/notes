# VLAN Trunking Protocol (VTP)

**VLAN Trunking Protocol (VTP)** is a Cisco proprietary Layer 2 protocol that propagates the definition of Virtual Local Area Networks (VLAN) on the whole LAN - reduces administration in a switched network.
**VTP** carries VLAN information ta all the switches in a **VTP domain**.
**VTP advertisements** can be sent over 802.1Q, and ISL trunks.

Using **VTP**, each Cisco Catalyst Family Switch advertises the following on its trunk ports:

- Management domain
- Configuration revision numbers
- Known VLANs and their parameters

[[Wikipedia - VTP](https://en.wikipedia.org/wiki/VLAN_Trunking_Protocol)]

### VTP Versions

Three VTP versions are available – V1, V2, and V3.<br>
V1 and V2 are similar except that V2 adds support for token ring VLANs.<br>

V3 adds the following features:

- Enhanced authentication
- Support for extended VLANs (1006 to 4094). VTP versions 1 and 2 can propagate only VLANs 1 to 1005.
- Support for private VLAN
- VTP primary server and VTP secondary servers
- VTP mode off that disables VTP
- Backward compatibility with VTP V1 and V2
- Ability to be configured on a per-port basis
