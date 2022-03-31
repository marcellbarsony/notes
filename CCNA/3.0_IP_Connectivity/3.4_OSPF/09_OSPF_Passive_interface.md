# OSPF Passive Interface

**OSPF** is a link-state routing protocol that creates and keeps neighbor relationships by sharing routing updates with other **OSPF Routers**.
No routing information is exchanged and the only packets they exchange are **OSPF Hello** packets.
**OSPF Hello** packets enables dynamic neighbor discovery and preserve neighbor connections.
**Passive interface** command is used to suppress **OSPF Hello** packets on a specified interface.
It is also used in other routing protocols like RIP and EIGRP.

Enabling **Passive interfaces** in our network devices mean that:

- **OSPF** continues to announce or advertise the interface’s connected network.
- **OSPF** routers stop sending **OSPF Hellos** on the interface.
- On the interface, **OSPF** no longer processes any received **Hellos**.

[[Study CCNA - OSPF Passive interface](https://study-ccna.com/ospf-passive-interface/)]

## Why Do We Use OSPF Passive Interface?

The passive interface should be configured on interfaces that do not have an OSPF router connected to them so that they won’t receive any OSPF information.
By silencing routing announcements on network interfaces, we tell the router to “listen but don’t talk”.
A protocol’s routing load on the CPU can be reduced by minimizing the number of interfaces with which it must interact.
The ‘passive-interface’ command disables OSPF and EIGRP route processing for that interface.
If you’re sure the routing protocol won’t need to communicate with anything on the specified interface, use this command.

Another reason to apply passive interface is to increase security.
An attacker could start an application that replies with OSPF hello packets then our router will try to establish neighbor relationship.
The attacker could then advertise fake routes to misdirect traffic.

## OSPF Passive Interface Configuration

There are two ways to configure OSPF passive interface in our network devices.

1. If we only need to configure passive interface on a single or a couple of interfaces, we can individually configure them using the `passive-interface` command:

```
Router#conf t
Router(config)#router ospf 1
Router(config-router)#passive-interface gi0/0/0
Router(config-router)#passive-interface gi0/0/1
```

2. All interfaces need to be passive interfaces and leave a single or a couple of interfaces non-passive.
   We can set passive interface as the default configuration by using the `passive-interface default` command:

```
Router#conf t
Router(config)#router ospf 1
Router(config-router)#passive-interface default
Router(config-router)#no passive-interface gi0/0/0
```

To verify our passive interface configuration, use the `show ip ospf interface command`.
