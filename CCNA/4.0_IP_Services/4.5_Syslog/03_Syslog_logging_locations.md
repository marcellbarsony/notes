# Syslog Logging Configuration

## Syslog Logging Configuration

**Syslog** messages can be logged to various locations.
There are 4 ways and locations where messages can be stored and displayed.

- **Logging Buffer** – Events saved in the RAM memory of a router or switches, the buffer has a fixed size to ensure that the log messages will not use up valuable system memory - it is enabled by default.
- **Console Line** – Events will be displayed in the CLI when you log in over a console connection - it is enabled by default.
- **Terminal Lines** – Log messages will be shown in the CLI when you log in over a Telnet or SSH session - it is disabled by default.
- **Syslog Server** – Log messages are saved in the Syslog server.

## Syslog Logging Configuration

### Logging Buffer Configuration

The **Logging Buffer** can be configured with the `logging buffered (buffer_size|severity_level)` command.

```
R1(config)#logging buffered
R1(config)#logging buffered 100000
R1(config)#logging buffered debugging
```

### Console Line Configuration

The Console Line Syslog configuration is enabled by default however, it can be disabled with the `no logging` command.

```
R1(config)#no logging console
```

### Terminal Line Configuration

Syslog can be configured to send messages into the VTY terminal lines using the `terminal monitor` command

```
R1(config)#terminal monitor
```

> Note<br>
> The reason terminal lines are disabled by default in Cisco IOS is because it might make your VTY terminal connections congested due to massive amounts of log messages being sent into the lines when it is improperly configured.

### Syslog Server Configuration

By default, logging messages are sent ot the logging host through UDP port 514.

Configure the **IP address of the Syslog Server** to be used by entering the `logging` command, then specify the **type of message** sent to the Syslog Server:

```
R1(config)#logging 10.0.0.100
R1(config)#logging trap debugging
```

Specify the **local timestamp** to use with the Syslog messages which will be sent ot the Syslog Server

```
R1(config)#service timestamps log datetime msec
```

The **Syslog logging configuration** can be verified with the `show logging` command.

### Security Information and Event Management (SIEM)

A **SIEM** can be thought of as a centralized log server as it provides a centralized location for all logging messages.
