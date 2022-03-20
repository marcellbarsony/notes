# Syslog

**Syslog** is a standard for message logging that allows separation of the software that generates messages, the system that stores them, and the software that reports and analyzes them.
Each message is labeled with a facility code, indicating the type os system generating the message, and is assigned a severity level.

When operating over a network, **Syslog** uses a client-server architecture where a **Syslog Server** listens for and logs messages coming from clients.

[[Wikipedia - Syslog](https://en.wikipedia.org/wiki/Syslog)]<br>
[[Study CCNA - Syslog explained](https://study-ccna.com/syslog-explained/)]<br>

## Enable Syslog

The `logging console` global configuration command is enabled by default.<br>
SSH and Telnet users need to execute the `terminal monitor` command to see system messages.

```
Router1#terminal monitor
```

It is recommended to store the generated logs to a central Syslog server.
To instruct a device to send logs to the Syslog server, we can use the `logging <ip_address>` or `logging host <hostname>` command:

```
Router1(config)#logging 10.0.0.10
```
