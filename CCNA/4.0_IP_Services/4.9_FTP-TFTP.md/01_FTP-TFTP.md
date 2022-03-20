# File Transfer Protocol (FTP)

**File Transfer Protocol (FTP)** is a standard communication protocol used for the transfer of computer files from a server to a client on a computer network.
**FTP** is built on a client-server model architecture using separate control and data connections between the client and the server.
**FTP** is often secured with SSL/TLS (FTPS) or replaced with [SSH File Transfer Protocol](https://en.wikipedia.org/wiki/SSH_File_Transfer_Protocol) (SFTP).

**FTP** uses two TCP ports: port 20 for sending data and port 21 for sending protocol commands.

[[Wikipedia - File Transfer Protocol](https://en.wikipedia.org/wiki/File_Transfer_Protocol)]

## Trivial File Transfer Protocol (TFTP)

**Trivial File Transfer Protocol (TFTP)** is a simple lockstep **FTP** which allow a client to get a file from or put a file onto a remote host.
**TFTP** is a simple version of **FTP**, lacking some features **FTP** offers, but requiring less resources.

**TFTP** does not support user authentication and sends all data in clear text via UDP port 69.

[[Wikipedia - Trivial File Transfer Protocol](https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol)]

## Copy files with FTP

Cisco IOS includes a built-in **FTP** client that cen bused to transfer images to and from the Cisco device.

The following steps are required for **FTP** transfers:

- Create an **FTP username and password** with the `ip ftp username <username>` and `ip ftp password <password>` command.
- Issue the `copy ftp flash` command and follow the wizard.
