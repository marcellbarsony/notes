## Curl

```sh
curl [Options] <url>
```

| Options | Description                      |
| ------- | -------------------------------- |
| -d      | POST data                        |
| -H      | Custom header                    |
| -I      | GET Response header              |
| -L      | Redirect                         |
| -o      | Download (specify file name)     |
| -O      | Download (original name)         |
| -v      | Verbose output (TLS handshake)   |

| Flags                   | Description      |
| ----------------------- | ---------------- |
| --cookie "key=value"    | Cookie set       |
| --data-binary @-        | POST binary file |
| --data-binary @file.txt | POST binary file |
