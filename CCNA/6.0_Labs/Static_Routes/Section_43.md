# Section 43 - Static Routes

## Step 1 - Configure Static Routes on R1

1. Configure Static Route to R3 on R1.

To reach R3, the route needs to be configured via R2 `192.168.2.2`.

At this point, R3 does not know how to route the reply back to R1.

```
R1(config)#ip route 192.168.3.0 255.255.255.0 192.168.2.2
```

2. Configure Static Route to R3's segment on R1.

To reach R3's segment, the route needs to be configure via R2 `192.168.2.2`.

Traffic sent from R1 to R3's subnet, firstly need to be sent through R2.

```
R1(config)#ip route 172.16.1.0 255.255.255.0 192.168.2.2
```

## Step 2 - Configure Static Routes on R2

1. Configure Static Route to R1's segment on R2.

To reach R1's segment, the route needs to be configure via R1 `192.168.2.1`.

Traffic sent from R2 to R1's subnet, firstly need to be sent through R1.

```
R2(config)#ip route 192.168.1.0 255.255.255.0 192.168.2.1
```

2. Configure Static Route to R3's segment on R2.

To reach R3's segment, the route needs to be configure via R3 `192.168.3.2`.

Traffic sent from R2 to R3's subnet, firstly need to be sent through R3.

```
R2(config)#ip route 172.16.1.0 255.255.255.0 192.168.3.2
```

## Step 3 - Configure Static Routes on R3

1. Configure Static Route to R1 on R3.

To reach R1', the route needs to be configure via R2 `192.168.3.1`.

```
R3(config)#ip route 192.168.2.0 255.255.255.0 192.168.3.1
```

2. Configure Static Route to R1's segment on R3.

To reach R1's segment, the route needs to be configure via R2 `192.168.3.1`.

```
R3(config)#ip route 192.168.1.0 255.255.255.0 192.168.3.1
```

## Step 4 - Configure S1

1. A Default Gateway needs to be configured to point to R1.

```
S1(config)#ip default-gateway 192.168.1.254
```

2. A Name Server needs to be configured on S1.

```
s1(config)#ip name-server 172.16.1.2
s1(config)#ip domain-lookup
```
