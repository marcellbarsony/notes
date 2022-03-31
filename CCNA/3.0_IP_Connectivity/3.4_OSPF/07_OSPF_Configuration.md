# OSPF Configuration

[[Study CCNA - OSPF Configuration](https://study-ccna.com/ospf-configuration/)]

## OSPF 1

1. Enable OSPF on the router with the `router ospf <process_id>` command

```
R1(config-router)#router ospf 1
```

> Note<br>
> The OSPF process number doesn't have to be the same on all routers in order to establish a neighbor relationship.<br>
> The Area ID has to be the same on all neighboring routers in order for routers to become neighbors.

2. Define on which interface(s) OSPF will run and what network(s) will be advertised with the `network <ip_address> <wildcard_mask> <area_id>` command

```
R1(config-router)#network 10.0.1.0 0.0.0.255 area 0
```

The network command entered include the directly connected subnets.<br>

### Verification

The **neighbor relationship** can be verified with the `show ip ospf neighbors` command.

The **exchanged routing updates** can be verified with the `show ip route command`.

## OSPF 2

**OSPF** provides many extra features that can be complex to set up.<br>
In this example, our router (**R2**) acts as **ABR (Area Border Router)** between area 0 (**R1**) and 1 (**R2**).

### Router 1

The goal is to advertise the subnets directly connected to **R1** and **R3** - to do that, the following configuration on **R1** is used:

```
R1(config)#router ospf 1
R1(config-router)#network 10.0.1.0 0.0.0.255 area 0
R1(config-router)#network 172.16.0.0 0.0.255.255 area 0
R1(config-router)#router-id 1.1.1.1
```

`router-id 1.1.1.1` is used to manually specify the router ID of the router.
OSPF process will use this RID when communicating with other OSPF neighbors.

### Router 3

Because **R1** connects only to **R2**, we only need to establish a neighbor relationship with **R2** and advertise directly connected subnet into OSPF.

Configuration of **R3** looks similar, but **R3** is in the area 1.

```
R1(config)#router ospf 1
R1(config-router)#network 192.168.0.0 0.0.0.255 area 1
R1(config-router)#network 90.10.0.0 0.0.0.255 area 1
R1(config-router)#router-id 3.3.3.3
```

### Router 2 (ABR)

As **R2** is an **ABR**, we need to establish neighbor relationship with both **R1** and **R3**.
We need to specify different area ID fo each neighbor relationship: 0 for **R1** and 1 for **R2**.

```
R1(config)#router ospf 1
R1(config-router)#network 172.176.0.0 0.0.255.255 area 0
R1(config-router)#network 192.168.0.0 0.0.0.255 area 1
R1(config-router)#router-id 2.2.2.2
```

Now, **R2** should have neighbor relationship with both **R1** and **R3**.

> Note<br>
> Since **R1** and **R3** reside in different areas, they never establish a neighbor relationship.
