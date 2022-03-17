# Configure DHCP

A Cisco router can be configured as a DHCP Server by taking the following steps:

1. **Exclude IP addresses** from being assigned by DHCP by using the `ip dhcp excluded-address <first_ip> <last_ip>` command.
2. Create a new **DHCP pool** with the `ip dhcp pool <name>` command.
3. Define a **Subnet** that will be used to assign IP addresses to hosts with the `network <subnet> <subnet_mask>` command.
4. Define the **Default gateway** with the `default-router <ip>` command.
5. Define the **DNS server** with the `dns-server <ip_address>` command.
6. (Optional) Define the **DNS domain name** by using the `ip domain-name <name>` command.
7. (Optional) Define the **Lease duration** by using the `lease <days> <hours> <minutes>` command.

## 1. Exclude IP addresses

IP addresses from `192.168.0.1` to `192.168.0.50` range will not be assigned to hosts.

```
R1(config)#ip dhcp excluded-address 192.168.0.1 192.168.0.50
```

## 2. DHCP Pool

Create DHCP pool with `ip dhcp pool <name>`

```
R1(config)#ip dhcp pool ?
  WORD  Pool name
R1(config)#ip dhcp pool pc
```

```
R1(dhcp-config)#?
  default-router  Default routers
  dns-server      Set name server
  domain-name     Domain name
  exit            Exit from DHCP pool configuration mode
  network         Network number and mask
  no              Negate a command or set its defaults
  option          Raw DHCP options
```

## 3. Subnet

Allocate the `network` with its subnet mask

```
R1(dhcp-config)#network 10.1.1.0 255.255.255.0
```

## 4. Default gateway

Specify a `default-router` (local router)

```
R1(dhcp-config)#default-router 10.1.1.254
```

## 5. DNS Server

Specify `dns-server` (local router)

```
R1(dhcp-config)#dns-server 10.1.1.254
```

## DHCP Configuration Information

```
R1#show ip dhcp ?
  binding   DHCP address bindings
  conflict  DHCP address conflicts
  pool      DHCP pools information
  relay     Miscellaneous DHCP relay information
```

### DHCP Binding

To view information about the currently leased addresses, use the `show ip dhcp binding` command.

The output shows that there is a single DHCP Client that was assigned the IP address of `192.168.0.51`.
Since we’ve excluded the IP addresses from the `192.168.0.1` – `192.168.0.50` range, the device got the first address available – `192.168.0.51`.

```
Floor1#show ip dhcp binding
IP address Client-ID/ Lease expiration Type
Hardware address
192.168.0.51 0060.5C2B.3DCC -- Automatic
```

### DHCP Pool

To display information about the configured DHCP pools, use the `show ip dhcp pool` command.

```
Floor1#show ip dhcp pool
Pool pc :
Utilization mark (high/low) : 100 / 0
Subnet size (first/next) : 0 / 0
Total addresses : 254
Leased addresses : 1
Excluded addresses : 1
Pending event : none

1 subnet is currently in the pool
Current index IP address range Leased/Excluded/Total
192.168.0.1 192.168.0.1 - 192.168.0.254 1 / 1 / 254
```
