# SSH Configuration

To enable secure access on a Cisco device, the following steps are required:

1. Set up a hostname and a domain name.

```
Router1(config)#hostname R1
R1(config)#ip domain-name cisco
```

2. Configure local username and password.

```
R1(config)#username study password ccna
```

3. Generate RSA public and private keys.

```
R1(config)#crypto key generate rsa
```

4. Allow SSH access only.

```
R1(config)#line vty 0 15
R1(config-line)#login local
R1(config-line)#transport input ssh
```

> Note<br>
> It is recommended to use SSH version 2 with the `ip ssh version 2` command.
