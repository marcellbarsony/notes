# Section 43 - Static Routes

## Step 1 - Configure R1

1. Configure sub-interface 1 (VLAN 1) on `g0/0/0`.

- Define encapsulation for the native VLAN (untagged, management VLAN).
- Define IP address for the sub-interface

```
R1(config)#int g0/0/0
R1(config-if)#no shut
R1(config-if)#exit
R1(config)#int g0/0/0.1
R1(config-subif)#encapsulation dot1Q 1 native
R1(config-subif)#ip address 10.1.1.254 255.255.255.0
```

- Check the configuration with `show run`

```
R1#show run
...
  interface GigabitEthernet0/0/0.1
   encapsulation dot1Q 1 native
   ip address 10.1.1.254 255.255.255.0
```

2. Configure sub-interface 2 (VLAN 10) on interface `g0/0/0`.

- Define encapsulation for VLAN 10.
- Define IP address for the sub-interface

```
R1(config)#interface g0/0/0.10
R1(config-subif)#encapsulation dot1Q 10
R1(config-subif)#ip address 10.1.10.254 255.255.255.0
```

3. Configure sub-interface 3 (VLAN 20) on interface `g0/0/0`.

- Define encapsulation for VLAN 20.
- Define IP address for the sub-interface

```
R1(config)#interface g0/0/0.20
R1(config-subif)#encapsulation dot1Q 20
R1(config-subif)#ip address 10.0.20.254 255.255.255.0
```

## Step 2 - Configure SW1

1. Configure VLAN 1.

```
S1(config)#interface vlan 1
S1(config-if)#no shut
S1(config-if)#ip address 10.1.1.253 255.255.255.0
```

2. Configure interface `g1/0/1` as a trunk port.

- Configure encapsulation (802.1Q)
- Configure trunk mode

```
S1(config)#interface g1/0/1
S1(config-if)#switchport trunk encapsulation dot1q
S1(config-if)#switchport mode trunk
```

- Verify the configuration

```
S1#show interfaces gigabitEthernet 1/0/1 switchport
```

2. Configure VLAN 10 and VLAN 20.

```
S1(config)#vlan 10
S1(config-vlan)#exit
S1(config)#vlan 20
```

3. Add the PCs to the VLANs.

- Add the PC on port `g1/0/2` to VLAN 10.

```
S1(config)#int g1/0/2
S1(config-if)#switchport mode access
S1(config-if)#switchport access vlan 10
```

- Add the PC on port `g1/0/3` to VLAN 20.

```
S1(config)#int g1/0/3
S1(config-if)#switchport mode access
S1(config-if)#switchport access vlan 20
```

## Step 3 - Configure S1

1. Configure Default Gateway pointing to R1 in the same subnet (10.1.1.254)

```
S1(config)#ip default-gateway 10.1.1.254
```

- At this point, S1 cannot ping PC1 nor PC2
- When `ip defualt-gateway` is used, `ip routing` must be disabled on a Layer 2 switch

```
S1(config)#no ip routing
```
