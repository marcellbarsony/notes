# Permissions

## Octal permissions

| Number | Permissions            | User | Group | Others |
| -----: | ---------------------- | :--: | :---: | :----: |
|      0 | No permission          | ---  |  ---  |  ---   |
|      1 | Execute                | --x  |  --x  |  --x   |
|      2 | Write                  | -w-  |  -w-  |  -w-   |
|      3 | Write + Execute        | -wx  |  -wx  |  -wx   |
|      4 | Read                   | r--  |  r--  |  r--   |
|      5 | Read + Execute         | r-x  |  r-x  |  r-x   |
|      6 | Read + Write           | rw-  |  rw-  |  rw-   |
|      7 | Read + Write + Execute | rwx  |  rwx  |  rwx   |

### Notes

1. SUID permission
2. SGID permission
3. Sticky bit

[The Geek Diary](https://www.thegeekdiary.com/what-is-suid-sgid-and-sticky-bit/)
