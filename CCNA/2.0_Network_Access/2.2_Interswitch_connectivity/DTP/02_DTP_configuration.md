# DTP configuration

Show DTP configuration on the specified interface

```
SW1#show dtp interface <interface>
```

### Switch port modes

- **Access** — Puts the Ethernet port into permanent nontrunking mode - does not act as a trunk interface, only allow one VLAN through the port - and negotiates to convert the link into a nontrunk link.
  The Ethernet port becomes a nontrunk port even if the neighboring port does not agree to the change.

```
SW1(config-if)#switchport mode access
```

- **Trunk** — Puts the Ethernet port into permanent trunking mode and negotiates to convert the link into a trunk link.
  The port becomes a trunk port even if the neighboring port does not agree to the change.

```
SW1(config-if)#switchport mode trunk
```

- **Dynamic Auto** — Makes the Ethernet port willing to convert the link to a trunk link.
  The port becomes a trunk port even if the neighboring port is set to trunk, dynamic desirable or dynamic auto mode.
  This is the default mode for some switchports.

```
SW1(config-if)#switchport mode dynamic auto
```

- **Dynamic Desirable** - Makes the port actively attempt to convert the link to a trunk link.
  The port becomes a trunk port if the neighboring Ethernet port is set to trunk, dynamic desirable or dynamic auto mode.

```
SW1(config-if)#switchport mode dynamic desirable
```

- **No-negotiate** - Disables DTP.<br>
  The port will not send out DTP frames or be affected by any incoming DTP frames.

```
SW1(config-if)#switchport nonegotiate
```

## DTP logical table

| SW1/SW2               | Dynamic Auto | Dynamic Desirable |        Trunk         |        Access        |
| --------------------- | :----------: | :---------------: | :------------------: | :------------------: |
| **Dynamic Auto**      |    Access    |       Trunk       |        Trunk         |        Access        |
| **Dynamic Desirable** |    Trunk     |       Trunk       |        Trunk         |        Access        |
| **Trunk**             |    Trunk     |       Trunk       |        Trunk         | Limited connectivity |
| **Access**            |    Access    |      Access       | Limited connectivity |        Access        |

- **Desirable** - The switch initiates trunking with the remote end
- **Auto** - Doesn't initiate but will use trunking if the other side initiates
