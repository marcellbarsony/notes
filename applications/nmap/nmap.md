# Usage


## Network scan


```sh
nmap 192.168.1.0/24
```

## Port scan

```sh
nmap -p- 10.98.1.0/24 # All
nmap -p 80,443 10.98.1.0/24 # Selected
nmap -p 1-100 10.98.1.0/24 # Range
```


