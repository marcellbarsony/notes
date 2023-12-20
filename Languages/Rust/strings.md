# Strings

Strings are implemented as a collection of bytes.

no null terminator (nullbyte)
all strings valid utf-8
immutable by default

## String types

### `&str` - String slice

Rust has only one string type (`str`) in the core language.<br>
String slice is usually seen in its borrowed form (`&str`);

- Description: A string slice is a reference to a portion of another string. It is immutable, meaning it cannot be changed.
- Storage: Stack
- Ownership: Borrowed (read only)
- Growability: Cannot grow
- Mutability: Immutable
- Encoding: UTF-8


### `String`

Provided by standard library (rather than coded into the core language).<br>
Growable, mutable, owned, UTF-8 encoded.

- Description: A growable, mutable string type. It is owned, meaning the data is stored on the heap and managed by the String object itself.
- Storage: Heap
- Ownership: Owned
- Growability: Can grow as needed
- Mutability: Mutable
- Encoding: UTF-8

- `Vec(u8)`
- `Cow<'a, str>`
- `CStr`
- `OsStr`
- `OsString`
- `Path`
- `PathBuff`

### `&(u8; N)`

    Description: A fixed-size slice of bytes. It is immutable and cannot contain Unicode characters.
    Storage: Stack or heap
    Ownership: Borrowed
    Growability: Cannot grow
    Mutability: Immutable
    Encoding: Byte-level

Vec<u8>

    Description: A dynamically-sized vector of bytes. It is mutable and can contain Unicode characters.
    Storage: Heap
    Ownership: Owned
    Growability: Can grow as needed
    Mutability: Mutable
    Encoding: Byte-level

Cow<'a, str>`

    Description: A clever data structure that can hold either a str slice or a String. This allows for efficient sharing of string data.
    Storage: Stack or heap
    Ownership: Owned or borrowed
    Growability: Dependent on the underlying data
    Mutability: Dependent on the underlying data
    Encoding: UTF-8

CStr

    Description: A raw string slice that represents a C-style string. It cannot be directly manipulated by Rust code.
    Storage: Stack
    Ownership: Borrowed
    Growability: Cannot grow
    Mutability: Immutable
    Encoding: Byte-level

OsStr

    Description: A raw string slice that represents a platform-specific string. It is similar to CStr but may have platform-specific limitations.
    Storage: Stack
    Ownership: Borrowed
    Growability: Cannot grow
    Mutability: Immutable
    Encoding: Byte-level

OsString

    Description: A growable, mutable raw string type. It is similar to Vec<u8> but is specifically designed for platform-specific strings.
    Storage: Heap
    Ownership: Owned
    Growability: Can grow as needed
    Mutability: Mutable
    Encoding: Byte-level

Path

    Description: A representation of a file or directory path. It can be constructed from raw strings or other Path objects.
    Storage: Stack
    Ownership: Owned
    Growability: Cannot grow
    Mutability: Mutable
    Encoding: Platform-specific

PathBuff

    Description: A mutable buffer for building or modifying Path objects. It provides efficient operations for adding, removing, and replacing segments of a path.
    Storage: Heap
    Ownership: Owned
    Growability: Can grow as needed
    Mutability: Mutable
    Encoding: Platform-specific


## Sources

- [Strings - The Rust Book](https://doc.rust-lang.org/book/ch08-02-strings.html)
