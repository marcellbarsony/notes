# STP Configuration

[[Cisco - Configure STP Settings on a Switch](https://www.cisco.com/c/en/us/support/docs/smb/switches/cisco-small-business-300-series-managed-switches/smb5760-configure-stp-settings-on-a-switch-through-the-cli.html)]

Enable Spanning Tree

```
SW1(config)#spanning tree
```

Configure STP protocol

```
SW1(config)#spanning-tree mode [stp|rstp|mst]
```

Set default path cost

```
SW1(config)#spanning-tree mode pathcost method [long|short]
```

Configure STP priority

```
SW1(config)#spanning-tree priority [priority number]
```

Configure how often the switch broadcasts Hello messages to other devices

```
SW1(config)#spanning-tree hello-time [seconds]
```

Configure STP maximum age

```
SW1(config)#spanning-tree max-age [seconds]
```

Configure the STP bridge forward time (which is the amount of time a port remains in the listening and learning states before entering the forwarding state)

```
SW1(config)#spanning-tree forward-time [seconds]
```

Enable STP Loopback Guard

```
SW1(config)#spanning-tree loopback-guard
```
