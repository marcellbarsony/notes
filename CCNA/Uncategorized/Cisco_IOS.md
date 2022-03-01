# Cisco IOS

Cisco IOS (Internetwork Operating System) is a multitasking operating system used on most Cisco routers and switches.
IOS has a command line interface with the predetermined number of multiple-word commands.
This system is used to configure features supported by a Cisco device.

### Modes

| Prompt          | Description          | Command                     |
| --------------- | -------------------- | --------------------------- |
| Router>         | User exec            | **Default**                 |
| Router#         | Privileged exec      | enable / en                 |
| Router(config)# | Global configuration | configure terminal / conf t |

<details>
<summary>User exec mode</summary>
<br>

| Command    | Description                         |
| ---------- | ----------------------------------- |
| <1-99>     | Session number to resume            |
| connect    | Open a terminal connection          |
| disable    | Turn off privileged commands        |
| disconnect | Disconnect existing connection      |
| enable     | Privileged mode                     |
| exit       | Exit from the EXEC                  |
| logout     | Exit from the EXEC                  |
| ping       | Send echo messages                  |
| resume     | Resume an active network connection |
| show       | Show running system information     |
| ssh        | SSH client connection               |
| telnet     | Telnet connection                   |
| terminal   | Set terminal line parameters        |
| traceroute | Trace route to destination          |

</details><br>

<details>
<summary>Privileged exec mode</summary>
<br>

| Command    | Description                                                 |
| ---------- | ----------------------------------------------------------- |
| <1-99>     | Session number to resume                                    |
| auto       | Exec level Automation                                       |
| clear      | Reset functions                                             |
| clock      | Manage the system clock                                     |
| configure  | Enter configuration mode                                    |
| connect    | Open a terminal connection                                  |
| copy       | Copy from one file to another                               |
| debug      | Debugging functions (see also 'undebug')                    |
| delete     | Delete a file                                               |
| dir        | List files on a filesystem                                  |
| disable    | Turn off privileged commands                                |
| disconnect | Disconnect an existing network connection                   |
| enable     | Turn on privileged commands                                 |
| erase      | Erase a filesystem                                          |
| exit       | Exit from the EXEC                                          |
| logout     | Exit from the EXEC                                          |
| mkdir      | Create new directory                                        |
| more       | Display the contents of a file                              |
| no         | Disable debugging information                               |
| ping       | Send echo messages                                          |
| reload     | Halt and perform a cold restart                             |
| resume     | Resume an active network connection                         |
| rmdir      | Remove existing directory                                   |
| send       | Send a message to other tty lines                           |
| setup      | Run the SETUP command facility                              |
| show       | Show running system information                             |
| ssh        | Open a secure shell client connection                       |
| telnet     | Open a telnet connection                                    |
| terminal   | Set terminal line parameters                                |
| traceroute | Trace route to destination                                  |
| undebug    | Disable debugging functions (see also 'debug')              |
| vlan       | Configure VLAN parameters                                   |
| write      | Write running configuration to memory, network, or terminal |

</details><br>

<details>
<summary>Global configuration mode</summary>
<br>

| Command           | Description                                      |
| ----------------- | ------------------------------------------------ |
| aaa               | Authentication, Authorization and Accounting.    |
| access-list       | Add an access list entry                         |
| banner            | Define a login banner                            |
| bba-group         | Configure BBA Group                              |
| boot              | Modify system boot parameters                    |
| cdp               | Global CDP configuration subcommands             |
| class-map         | Configure Class Map                              |
| clock             | Configure time-of-day clock                      |
| config-register   | Define the configuration register                |
| crypto            | Encryption module                                |
| default           | Set a command to its defaults                    |
| do                | To run exec commands in config mode              |
| dot11             | IEEE 802.11 config commands                      |
| enable            | Modify enable password parameters                |
| end               | Exit from configure mode                         |
| exit              | Exit from configure mode                         |
| flow              | Global Flow configuration subcommands            |
| hostname          | Set system's network name                        |
| interface         | Select an interface to configure                 |
| ip                | Global IP configuration subcommands              |
| ipv6              | Global IPv6 configuration commands               |
| key               | Key management                                   |
| license           | Configure license features                       |
| line              | Configure a terminal line                        |
| lldp              | Global LLDP configuration subcommands            |
| logging           | Modify message logging facilities                |
| login             | Enable secure login checking                     |
| mac-address-table | Configure the MAC address table                  |
| no                | Negate a command or set its defaults             |
| ntp               | Configure NTP                                    |
| parameter-map     | parameter map                                    |
| parser            | Configure parser                                 |
| policy-map        | Configure QoS Policy Map                         |
| port-channel      | EtherChannel configuration                       |
| priority-list     | Build a priority list                            |
| privilege         | Command privilege parameters                     |
| queue-list        | Build a custom queue list                        |
| router            | Enable a routing process                         |
| secure            | Secure image and configuration archival commands |
| security          | Infra Security CLIs                              |
| service           | Modify use of network based services             |
| snmp-server       | Modify SNMP engine parameters                    |
| spanning-tree     | Spanning Tree Subsystem                          |
| tacacs-server     | Modify TACACS query parameters                   |
| username          | Establish User Name Authentication               |
| vpdn              | Virtual Private Dialup Network                   |
| vpdn-group        | VPDN group configuration                         |
| zone              | FW with zoning                                   |
| zone-pair         | Zone pair command                                |

Beginning with IOS 12.3, **privileged exec mode** commands can be executed within **global configuration mode** and its submodes with the `do` keyword.

</details><br>

<details>
<summary>Additional useful commands</summary>
<br>

| Command                                                     | Description                                | Mode       |
| ----------------------------------------------------------- | ------------------------------------------ | ---------- |
| ?                                                           | Available commands (help)                  | all        |
| show version **/** sh ver                                   | Show software version                      | #          |
| hostname <value> **/** host <value>                         | Hostname configuration                     | config     |
| copy running-config startup-config **/** wr                 | Save configuration                         | #          |
| show ip interface brief                                     | Show current interface configuration       | #          |
| show running-config                                         | Show current configuration                 | #          |
| show cdp neighbors                                          | CDP neighbors                              | #          |
| show arp                                                    | Show ARP table                             | #          |
| int g0/0/0                                                  | Configure interface GE 0/0/0               |            |
| interface GigabitEthernet 0/0/0                             | Configure interface GE 0/0/0               |            |
| no shut **/** no shutdown                                   | No shutdown                                |            |
| no ip address                                               | Remove configure ip address from interface | config-if# |
| ip domain-lookup                                            |                                            |            |
| ip name-server <ip_address>                                 | Set IP name server                         |            |
| ip default gateway <ip_address>                             | Default Gateway                            | config     |
| monitor session 1 source interface gigabitEthernet 0/0      | Copy traffic from source interface         | config     |
| montior session 1 destination interface gigabitEthernet 0/0 | Duplicate traffic to destination interface | config     |

### Password

| Command                     | Description                | Mode   |
| --------------------------- | -------------------------- | ------ |
| enable password <password>  | Enable password            | config |
| service password-encryption | Enable password encryption | config |
| enable secret <password>    | Enable secret password     | config |

</details><br>

### Running & Startup configuration

Cisco devices store commands in two configuration files:

- Startup configuration
- Running configuration

The commands typed in the interface are stored in the **running configuration**.<br>
The **running configuration** resides in the devices's RAM.

The following commands will copy the **running configuration** to the **startup configuration**

```
copy running-config startup-config
```

```
wr
```
