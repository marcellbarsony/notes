# Access Control List (ACL)

In computer security, an **Access-Control List (ACL)** is a list of [Access Control Entries (ACE)](https://docs.microsoft.com/en-us/windows/win32/secauthz/access-control-entries) associated with a [system resource](https://en.wikipedia.org/wiki/System_resource).
Each **ACE** in an **ACL** identifies a trustee and specifies the access rights allowed, denied, or audited for that trustee.
The security descriptor for a securable object can contain two types of **ACLs**: a **DACL** and a **SACL**.

## Discretionary Access Control List (DACL)

A **Discretionary Access Control List (DACL)** identifies the trustees that are allowed or denies access to a securable object.
When a process tries to access a securable object, the systems checks the **ACEs** in the object's **DACL** to determine whether to grant access to it.

- If the object does not have a **DACL**, the system grants full access to everyone.
- If the object's **DACL** has no **ACEs**, the system denies all attempts to access the object because the **DACL** does not allow any access rights.

The system checks the ACEs in sequence until it finds one more ACEs that allow all the requested access rights, or until any of the requested access rights are identified.

## System Access Control List (SACL)

A **System Access Control List (SACL)** enables administrators to log attempts to access a secured object.
Each ACE specifies the types of access attempts by a specified trustee that cause the system to generate a record in the security event log.
An ACE in a **SACL** can generate audit records when an access attempt fails, when it succeeds, or both.

[[Microsoft - Access Control Lists](https://docs.microsoft.com/en-us/windows/win32/secauthz/access-control-lists)]<br>
[[Wikipedia - Access-control list](https://en.wikipedia.org/wiki/Access-control_list)]<br>
[[Study CCNA - What are ACLs?](https://study-ccna.com/what-are-acls/)]<br>

## ACL Process

An Access List is a sequential list of statements where packets are evaluated from the first statement to the last statement (top down).<br>
Of a packet is matched by an individual statement in the access list, that packet will be either **permitted** or **denied**, depending on whether the permit or deny keyword is used in that specific statement - all remaining lines of the Access List are ignored for that specific packet.
If the packet does not match the specific line or statement, then the next line in the **ACL** is checked.
If the packet does not match with the ACL, then the packet is dropped (implicit denial).

### Standard ACL

**Standard ACL**s only check on source IP addresses - they do no th check on individual port numbers or individual protocols.
**Standard ACL**s either permit or deny the entire protocol suite based on the source IP address or source network.
Nothing else than the source IP address or source network can be specified.

### Extended ACL

**Extended ACL**s check on the source and destination IP addresses.
**Extended ACL**s can permit or deny specific ports or applications (Ports: 80, 23, 21, 20. Protocols: IP, TCP, UDP, ICMP).
