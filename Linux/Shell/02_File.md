# File

## Commands

| Commands | Description                                   |
| -------- | --------------------------------------------- |
| cat      | Output file content                           |
| cp       | Copy
| file     | File information
| gpg      | Decrypt file
| gpg -c   | Encrypt file
| head     | Output file content (first 10 line)
| less     | Output file content
| ls       | List Directories
| ln -s    | Symbolic Link
| ls -la   | List Directories
| more     | Output file content
| mkdir    | Create directory
| mv       | Move
| rm       | Remove file
| rm -f    | Force Remove
| rm -r    | Remove Recursively
| rm -rf   | Force Remove Recursively
| touch    | Create File
| tail     | Output file content (last 10 line)
| wc       | Number of lines, words and bytes

## Permissions

| Command | Description             |
| ------- | ----------------------- |
| chmod   | Change file permissions |
| chown   | Change fiel ownership   |

| Octal | Permission |
| :---: | ---------- |
| 4     | Read       |
| 2     | Write      |
| 1     | Execute    |

Order: `owner`/`group`/`world`

## Archive & Compression

### Tar (Archive)

| Command                            | Description                       |
| ---------------------------------- | --------------------------------- |
| cf                                 | Tar file                          |
| xf                                 | UnTar file                        |
| c                                  | Create archive                    |
| f                                  | Specify filename                  |
| j                                  | bzip2 compression                 |
| k                                  | Don't overwrite                   |
| t                                  | Table of contents                 |
| v                                  | Verbose                           |
| w                                  | Ask for confirmation              |
| x                                  | Extract                           |
| z                                  | Zip/Gzip                          |

### Gunzip (Compression)

| Command                            | Description                       |
| ---------------------------------- | --------------------------------- |
| gzip                               | Compress file                     |
| gzip -d                            | Decompress file                   |
