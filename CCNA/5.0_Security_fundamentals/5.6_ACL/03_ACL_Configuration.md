# Access Control List Configuration

[[Study CCNA - Configuring Extended ACLs](https://study-ccna.com/configuring-extended-acls/)]

## Standard ACL Configuration

**Standard Access Control Lists** are configured in 2 steps in a Cisco device:

1. **ACL** is created with the `access-list` command in global configuration mode

```
R1(config)# access-list <ACL_NUMBER> <permit|deny> <IP_ADDRESS> <WILDCARD_MASK>
```

```
R1(config)# access-list <ACL_NUMBER> <permit|deny> host <IP_ADDRESS>
```

2. **ACL** is applied to an inbound or outbound interface with the `access-group` command

```
R1(config)#int fa0/0
R1(config-if)#ip access-group <ACL_NUMBER> <in|out>
```

## Extended ACL Configuration

With **Extended Access Control Lists**, additional packet information can be evaluated:

- Source and destination IP address
- TCP/IP protocol type (TCP, UDP, IP, etc.)
- Source and destination port numbers

**Extended Access Control Lists** are configured in 2 steps:

1. **Extended ACL** is created

```
R1(config)#access list <NUMBER> <permit|deny> <IP_PROTOCOL> <SOURCE_ADDRESS> <WILDCARD_MASK> [PROTOCOL_INFORMATION] <DESTINATION_ADDRESS> <WILDCARD_MASK> <PROTOCOL_INFORMATION>
```

2. **Extended ACL** is applied to an interface

```
R1(config)#ip access-group <ACL_NUMBER> <in|out>
```

## Named ACL Configuration

**Named ACL**s have the following advantages over numbered ACLs:

- A meaningful name can be assigned to the ACL
- ACL subcommands are used in ACL configuration mode - and not in the global configuration mode as with numbered ACLs
- Statements can be reordered using sequence numbers

The **Named ACL** name and type is defined using the following syntax

```
R1(config)#ip access-list <STANDARD|EXTENDED> <NAME>
```

This command moves you to the ACL configuration mode, where we can configure the _permit_ and _deny_ statements.
ACLs end with implicit _deny_ statement - any traffic not explicitly permitted will be forbidden.
