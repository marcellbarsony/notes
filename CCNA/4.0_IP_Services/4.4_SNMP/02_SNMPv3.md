# SNMPv3 Overview and Configuration

The latest version is **SNMP version 3 (SNMPv3)**, wherein it addresses the weaknesses of the earlier SNMP versions, such as security problems, by adding cryptographic security features wherein its developers have been able to make things look much different by introducing new conventions, concepts, and terminology.

[[Study CCNA - SNMPv3 Overview and Configuration](https://study-ccna.com/snmpv3-overview-configuration/)]

## SNMPv3 Features

The SNMPv3 architecture introduces the **User-based Security Model (USM)** for message security.
With **USM**, the messages exchanged between the SNMP Manager and the SNMP Agent will have data integrity checking and data origin authentication.

The **View-Based Access Control Model (VACM)** is for message processing models and access control.

**SNMPv3** supports the SNMP ‘**Engine ID**’ Identifier, which uniquely identifies each SNMP entity.
Conflicts can occur if two SNMP entities have duplicate **EngineID**’s.
The **EngineID** is used to generate the key for authenticated messages.

Many SNMP products remain fundamentally the same under SNMPv3 but are enhanced by the following new features:

### Security

- Authentication
- Privacy

### Administration

- Authorization and access control
- Logical contexts
- Naming of entities, identities, and information
- People and policies
- Usernames and key management
- Notification destinations and proxy relationships
- Remote configuration via SNMP operations

## SNMPv3 Elements

There are three new elements introduced in SNMPv3, that are working hand in hand with each other to provide a higher level of security by authenticating and encrypting every interaction with the network device.

**SNMP View** – defines what you can see on a Cisco device. This SNMPv3 element makes sure that unauthorized users are not able to see sensitive information while in the network, such as passwords, for example.

**SNMP User** – in SNMPv3, an SNMP User is then associated to an SNMP Group wherein it is added to it so that the access and views are limited. While associating the User to the Group, the username is defined, the password, as well as the level of encryption and authentication.

**SNMP Group** – SNMP View is associated with an SNMP Group wherein it defines the type of access such as read-only or read/write. The type of security method to be enabled during the interaction with a device is specified by SNMP Group.

SNMPv3 security models come primarily in two forms: Authentication and Encrypting.

- **Authentication** – is used to ensure that traps are read by only the intended recipient.
  As messages are created, they are given a special key that is based on the EngineID of the entity.
  The key is shared with the intended recipient and used to receive the message.

- **Encrypting** – privacy encrypts the payload of the SNMP message to ensure that it cannot be read by unauthorized users.
  Any intercepted traps will be filled with garbled characters and will be unreadable.
  Privacy is especially useful in applications where SNMP messages must be routed over the Internet.

There are three security levels in an SNMP Group:

1. **noAuthnoPriv** – Communication without authentication and privacy.

2. **authNoPriv** – Communication with authentication and without privacy.
   The protocols used for Authentication are MD5 and SHA (Secure Hash Algorithm).

3. **authPriv** – Communication with authentication and privacy.
   The protocols used for Authentication are MD5 and SHA, and for Privacy, DES (Data Encryption Standard) and AES (Advanced Encryption Standard) protocols can be used.
   For Privacy Support, you have to install some third-party privacy packages.
