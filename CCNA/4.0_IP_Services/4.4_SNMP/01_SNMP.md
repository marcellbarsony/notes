# Simple Network Management Protocol (SNMP)

**Simple Network Management Protocol (SNMP)** is an internet standard application layer protocol for collecting and organizing information about managed devices on IP networks and ofr modifying that information tha change device behavior.

**SNMP** exposes management data in the form of variables on the manged systems organized in a management information base (MIB) which describe the system status and configuration.
These variables can then be remotely queried and manipulated by managing applications.

An **SNMP**-managed network consists of two components:

- **Network Management Station (NMS)** — The software which runs on the administrative computer.
  **NMS** gathers **SNMP** data by requireing the devices on the network to disclose certain information.
  Devices can also inform **NMS** about problems they are experiencing by sending **SNMP** alert (called a trap).
  **NMS** uses UDP port 162.

- **Agent** — The software which runs on managed devices and reports information via **SNMP** to the **NMS**.
  **SNMP Agent** use UDP port 161.

[[Wikipedia - Simple Network Management Protocol](https://en.wikipedia.org/wiki/Simple_Network_Management_Protocol)]<br>
