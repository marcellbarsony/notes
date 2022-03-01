# Configure duplex and speed

By default, Cisco switches will auto-negotiate the speed and duplex settings.<br>
When a device (either a switch, router, or a workstation) is connected to a port on a Cisco switch, the negotiation process will occur and the devices will agree on the transmission parameters.

<img src="https://www.dropbox.com/s/fc6unctru353fow/auto_negotiation.jpg?dl=1" alt="auto_negotiation" class="inline" />

In the picture above there is a network of a hub, a switch, and a workstation with auto-negotiation turned on.<br>
Because hubs can only operate in half duplex, the switch and hub will negotiate to use the speed of 100 Mbps and half-duplex.
The workstation on the right is capable of 100 Mbps and supports full duplex, so the devices will use these parameters to communicate.

### Verify settings

We can verify the speed and duplex settings using the show interface command on SW1:

```
SW1#show interface Fa0/1
FastEthernet0/1 is up, line protocol is up (connected)
Hardware is Lance, address is 0009.7c66.6401 (bia 0009.7c66.6401)
...
Half-duplex, 100Mb/s
...
SW1#show int fa0/2
FastEthernet0/2 is up, line protocol is up (connected)
Hardware is Lance, address is 0009.7c66.6402 (bia 0009.7c66.6402)
...
Full-duplex, 100Mb/s
...
```

As show in the output above, the interface Fa0/1 will use the speed of 100 Mbps and half-duplex.<br>
The Fa0/2 interface will use the same speed, but it will use the full duplex communication.

### Set Duplexity and Speed

It is recommended that devices on both sides of a link should have auto-negotiation turned on, or both sides should have it off.
**Speed** and **duplex** parameters can also be configured manually with the `speed` and `duplex` commands in interface mode:

```
SW1(config)#int Fa0/3
SW1(config-if)#speed 100
SW1(config-if)#duplex full
```

If one device uses autonegotiation and the other one has disabled it, the device using autonegotiation will choose the default duplex setting based on the current speed.
The defaults are:

- If the speed is not known, 10 Mbps and half duplex settings will be used.

If the device successfully senses the speed without IEEE autonegotiation, by just looking at the signal on the cable:

- If the speed is 10 or 100 Mbps, use half duplex.
- If the speed is 1,000 Mbps or faster, use full duplex.

[[Study CCNA](https://study-ccna.com/configure-speed-and-duplex/)]
