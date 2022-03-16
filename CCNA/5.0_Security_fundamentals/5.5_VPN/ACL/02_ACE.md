# Access Control Entries

An **Access Control Entry (ACE)** is an element in an Access Control List (ACL).
An ACL can have zero or more **ACE**s.
Each **ACE** controls or monitors access to an object by a specified trustee.

There are six types of **ACE**s, three of which are supported by all securable objects.
The other three types are Object-specific **ACE**s supported by directory service objects.

All types of ACEs contain the following access control information:

- A **[Security Identifier (SID)](https://docs.microsoft.com/en-us/windows/win32/secauthz/security-identifiers)** that identifies the trustee to which the **ACE** applies.
- An **[Access Mask](https://docs.microsoft.com/en-us/windows/win32/secgloss/a-gly)** that specifies the access rights controlled by the ACE.
- A **Flag** that indicates the type of ACE.
- A set of **Bit Flags** that determine whether child containers or objects can inherit the **ACE** from the primary object to which the ACL is attached.

## ACE types supported by all securable objects.

| Type               | Description                                                                                                                                |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Access-denied ACE  | Used in a discretionary access control list (DACL) to deny access rights to a trustee.                                                     |
| Access-allowed ACE | Used in a DACL to allow access rights to a trustee.                                                                                        |
| System-audit ACE   | Used in a system access control list (SACL) to generate an audit record when the trustee attempts to exercise the specified access rights. |

[[Microsoft - Access Control Entries](https://docs.microsoft.com/en-us/windows/win32/secauthz/access-control-entries)]
