# Syslog Message Format

## Message Components

### Facility

A facility code is used to specify the type of system that is logging the message.
Messages with different facilities may be handled differently.

| Facility code | Keyword         | Description                              |
| ------------- | --------------- | ---------------------------------------- |
| 0             | kern            | Kernel messages                          |
| 1             | user            | User-level messages                      |
| 2             | mail            | Mail system                              |
| 3             | daemon          | System daemons                           |
| 4             | auth            | Security/authentication messages         |
| 5             | syslog          | Messages generated internally by syslogd |
| 6             | lpr             | Line printer subsystem                   |
| 7             | news            | Network news subsystem                   |
| 8             | uucp            | UUCP subsystem                           |
| 9             | cron            | Cron subsystem                           |
| 10            | authpriv        | Security/authentication messages         |
| 11            | ftp             | FTP daemon                               |
| 12            | ntp             | NTP subsystem                            |
| 13            | security        | Log audit                                |
| 14            | console         | Log alert                                |
| 15            | solaris-cron    | Scheduling daemon                        |
| 16–23         | local0 – local7 | Locally used facilities                  |

### Severity level

The list of severities defined by the standard

| Value | Severity      | Keyword | Deprecated keywords | Description                       | Condition                                                                              |
| ----- | ------------- | ------- | ------------------- | --------------------------------- | -------------------------------------------------------------------------------------- |
| 0     | Emergency     | emerg   | panic               | System is unusable                | A panic condition.                                                                     |
| 1     | Alert         | alert   | -                   | Action must be taken immediately  | A condition that should be corrected immediately, such as a corrupted system database. |
| 2     | Critical      | crit    | -                   | Critical conditions               | Hard device errors.                                                                    |
| 3     | Error         | err     | error               | Error conditions                  | -                                                                                      |
| 4     | Warning       | warning | warn                | Warning conditions                | -                                                                                      |
| 5     | Notice        | notice  | -                   | Normal but significant conditions | Conditions that are not error conditions, but that may require special handling.       |
| 6     | Informational | info    | -                   | Informational messages            | Confirmation that the program is working as expected.                                  |
| 7     | Debug         | debug   | -                   | Debug-level messages              | Messages that contain information normally of use only when debugging a program.       |
