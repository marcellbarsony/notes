# Penetration Testing Lab

## Lab Components

### 01 - Hypervisor

- [[VirtualBox](https://www.virtualbox.org/)]<br>
- [[VMware Workstation Player](https://www.vmware.com/hu/products/workstation-player/workstation-player-evaluation.html)]<br>

### 02 - Attacking VM

- [[Kali Linux](https://www.kali.org/)]<br>
- [[Parrot OS](https://www.parrotsec.org/)]<br>

### 03 - Vulnerable VM

- [[VulnHub](https://www.vulnhub.com/)]<br>

### 04 - Virtual Firewall [Optional]

- [[pfSense](https://www.pfsense.org/)]<br>

## Network Settings

### Isolated Network

The **Attacking VM** and the **Vulnerable VM** must be isolated.

VMs must be placed onto the same internal network.

- Network adapter settings: Internal Network

### DHCP Server

```
vboxmanage dhcpserver add --network=<internal_network_name> --server-ip=10.38.1.1 --lower-ip=10.38.1.110 --upper-ip=10.38.1.120 --netmask=255.255.255.0 --enable
```

### Test

- Test if the machines has IP address assigned
- Test if the machine has external network access
