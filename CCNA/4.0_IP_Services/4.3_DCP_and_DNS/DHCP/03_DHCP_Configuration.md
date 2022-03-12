# Configure DHCP

## Show DHCP Configuration

```
R1#show ip dhcp ?
  binding   DHCP address bindings
  conflict  DHCP address conflicts
  pool      DHCP pools information
  relay     Miscellaneous DHCP relay information
```

## Configure DHCP Pool

1. Create DHCP pool

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

### DHCP Pool configuration

1. Allocate the `network` with its subnet mask

```
R1(dhcp-config)#network 10.1.1.0 255.255.255.0
```

3. Specify a `default-router` (local router)

```
R1(dhcp-config)#default-router 10.1.1.254
```

3. Specify `dns-server` (local router)

```
R1(dhcp-config)#dns-server 10.1.1.254
```
