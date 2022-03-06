# Section 38

## Step 1

Configure hostname on **Core1**, **Core2**, **Access1**, **Access2**, **Access3**, **IntRouter**.

```
Switch#conf terminal
Enter configuration commands, one per line.  End with CNTL/Z.
Switch(config)#hostname Core1
Core1(config)#
```

## Step 2

Shut down unused interfaces on SW **Core1** and **Core2**, router **IntRouter** and on the **Access Switches**.

```
Core1(config)#interface range gigabitEthernet 1/0/4 - 19
Core1(config-if-range)#shut
```

Verify the changes with the `Core1#show ip interface brief ` command

> Note<br>
> Shut down multiple interfaces with the `range` command

## Step 3

Enable interface GigabitEthernet 0/0/0 and 0/0/1 on **IntRouter**.

```
IntRouter(config)#interface gig 0/0/0
IntRouter(config-if)#no shut
IntRouter(config-if)#interface gig 0/0/1
IntRouter(config-if)#no shut
```

Shut down unused interfaces.

## Step 4

Configure enable password of `cisco`.

```
Core1(config)#enable password cisco
```

Configure secret password of `cisco`.

```
Core1(config)#enable secret cisco
```

> Note<br>
> It is recommended to use a secret password rather than an enable password.

## Step 5

Configure VTY lines.

```
Core1(config)#line vty 0 4
Core1(config-line)#login
% Login disabled on line 1, until 'password' is set
% Login disabled on line 2, until 'password' is set
% Login disabled on line 3, until 'password' is set
% Login disabled on line 4, until 'password' is set
% Login disabled on line 5, until 'password' is set
Core1(config-line)#password cisco
Core1(config-line)#
```

> Note<br>
> Both `login` and `password cisco` commands are needed to configure VTY lines.<br>
> The order of the commands doesn't matter.

## Step 6

Use VTP mode `transparent` and set VTP domain name `ccna`.

```
Core1(config)#vtp mode transparent
  Setting device to VTP TRANSPARENT mode.
Core1(config)#vtp domain ccna
  Changing VTP domain name from NULL to ccna
```

Verify VTP configuration.

```
Core1#show vtp status
```

> Note<br>
> VTP must not be configured on a Router as it is a Layer 3 device.

## Step 7

Configure VLANs `10`, `20`, `30`, `100` to the VLAN database.

```
Core1(config)#vlan 10
Core1(config-vlan)#vlan 20
Core1(config-vlan)#vlan 30
Core1(config-vlan)#vlan 100
```

Verify VLAN configuration.

```
Core1#show vlan brief
```

> Note<br>
> VLANs must not be configured on a Router as it is a Layer 3 device.

## Step 8

Configure ports as Trunk ports between switches:

- Configure trunk encapsulation (dot1q)
- Configure trunk port

```
Core1(config)#interface range gig 1/0/1-3
Core1(config-if-range)#switchport trunk encapsulation dot1q
Core1(config-if-range)#switchport mode trunk
```

Verify the configuration with the `Core1(config-if-range)#do show run` command.

## Step 9

Configure ports as Access ports on links to PCs, to the Server, and to the IntRouter..

```
Access1(config)#interface gigabitEthernet 1/0/1
Access1(config-if)#switchport mode access
Access1(config-if)#switchport access vlan 10
```

Verify the switchport configuration with the `Access1#show interfaces g1/0/1 switchport` command.
