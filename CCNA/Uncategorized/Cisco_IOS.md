## Cisco IOS

### Modes

| Prompt    | Description          | Command                     |
| --------- | -------------------- | --------------------------- |
| >         | User                 | **Default**                 |
| #         | Privileged           | enable / en                 |
| (config)# | Global configuration | configure terminal / conf t |

<details>
<summary>User mode</summary>
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
<summary>Privileged mode</summary>
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

| Command                                     | Description                                | Mode       |
| ------------------------------------------- | ------------------------------------------ | ---------- |
| ?                                           | Available commands (help)                  | all        |
| show version **/** sh ver                   | Show software version                      | #          |
| hostname <value> **/** host <value>         | Hostname configuration                     | config     |
| copy running-config startup-config **/** wr | Save configuration                         | #          |
| show ip interface brief                     | Show current interface configuration       | #          |
| show running-config                         | Show current configuration                 | #          |
| show cdp neighbors                          | CDP neighbors                              | #          |
| show arp                                    | Show ARP table                             | #          |
| int g0/0/0                                  | Configure interface GE 0/0/0               |            |
| interface GigabitEthernet 0/0/0             | Configure interface GE 0/0/0               |            |
| no shut **/** no shutdown                   | No shutdown                                |            |
| no ip address                               | Remove configure ip address from interface | config-if# |
| ip domain-lookup                            |                                            |            |
| ip name-server <ip_address>                 | Set IP name server                         |            |
| ip default gateway <ip_address>             | Default Gateway                            | config     |

### Password

| Command                     | Description                | Mode   |
| --------------------------- | -------------------------- | ------ |
| enable password <password>  | Enable password            | config |
| service password-encryption | Enable password encryption | config |
| enable secret <password>    | Enable secret password     | config |
