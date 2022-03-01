# Knowledge Base

### Knowledge Base Icons

| Icon                 | Description                                                       |
| -------------------- | ----------------------------------------------------------------- |
| :pencil:             | QIDs edited by manager user                                       |
| :wi-fi antenna:      | Authentication is not required for remote vulnerability detection |
| :key:                | Authentication is required for remote vulnerability detection     |
| :red cross:          | Patchable vulnerability                                           |
| :fedora:             | Vulnerabilities happened on exploit                               |
| :hazardous material: | Vulnerabilities associated with malware                           |
| :cogwheel:           | Not exploitable due to configuration                              |
| :hexagon:            | Vulnerabilities associated with non-running services              |

### Severity

| Color      | Description                                  | Description                                     |
| ---------- | -------------------------------------------- | ----------------------------------------------- |
| Red        | Confirmed Vulnerability                      | Security weakness verified by an "active test"  |
| Yellow     | Potential Vulnerability                      | Security weakness requiring manual verification |
| Blue       | Information Gathered                         | Configuration data                              |
| Red/Yellow | Result will vary depending on authentication |                                                 |

| Severity Level | Description                                                                                                                                                                                                        |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 - Minimal    | Intruders can collect information about the host via open ports or services, which can lead to the disclosure of other vulnerabilities.                                                                            |
| 2 - Medium     | Intruders can collect sensitive information from the host, such as software versions installed, which can reveal known vulnerabilities.                                                                            |
| 3 - Serious    | Intruders can gain access to security settings on the host, which could lead to: access to files and disclosure of file contents, directory browsing, denial of service attacks, and unauthorized use of services. |
| 4 - Critical   | Intruders can potentially gain control of the host, or collect highly sensitive information including: R access to files, potential backdoors, or a listing of all user accounts on the host.                      |
| 5 - Urgent     | Intruders can easily gain control of the host, which can lead to the compromise of the entire network. Vulnerabilities include: RW access to files, remote code execution, and backdoors.                          |
