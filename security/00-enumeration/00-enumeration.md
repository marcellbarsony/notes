# Enumeration

## References

- [](https://github.com/mza7a/pentest-checklist?tab=readme-ov-file#enumeration)

- [Nmap - man page](https://linux.die.net/man/1/nmap)

## Enumeration

Target IP(s)
```sh
nmap
```

Open ports
```sh
# All 65,535 ports
nmap -p- <target_ip>

# Specific port
nmap -p <port> <target_ip>

# Range of ports
nmap -p <port>,<port> <target_ip>
```

Operating system
```sh
nmap -O <target_ip>
```

### Services

Probe open ports to determine service/version info
```sh
nmap -sv <target_ip>
```

Subdomains
