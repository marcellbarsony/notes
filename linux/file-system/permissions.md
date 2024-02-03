# Permissions

<!-- {{{ ## Octal permissions -->
## Octal permissions

| Numeric | User  | Group | World |
| :------ | :---: | :---: | :---: |
| 777     |  rwx  |  rwx  |  rwx  |
| 755     |  rwx  |  r-x  |  r-x  |
| 700     |  rwx  |  ---  |  ---  |
| 666     |  rw-  |  rw-  |  rw-  |
| 644     |  rw-  |  r--  |  r--  |
| 600     |  rw-  |  ---  |  ---  |
| 555     |  r-x  |  r-x  |  r-x  |
| 500     |  r-x  |  ---  |  ---  |
| 444     |  r--  |  r--  |  r--  |
| 400     |  r--  |  ---  |  ---  |
| 333     |  ---  |  w--  |  w--  |
| 300     |  ---  |  w--  |  ---  |
| 222     |  ---  |  ---  |  x--  |
| 200     |  ---  |  ---  |  x--  |
| 111     |  ---  |  t--  |  t--  |
| 100     |  ---  |  t--  |  ---  |
| 077     |  ---  |  rwx  |  rwx  |
| 060     |  ---  |  rw-  |  ---  |
| 055     |  ---  |  r-x  |  ---  |
| 040     |  ---  |  r--  |  ---  |
| 000     |  ---  |  ---  |  ---  |

### Notes

1. SUID permission
2. SGID permission
3. Sticky bit

[The Geek Diary](https://www.thegeekdiary.com/what-is-suid-sgid-and-sticky-bit/)
<!-- }}} -->
