# Error handling

[Error Handling - The Rust Book](https://doc.rust-lang.org/book/ch09-00-error-handling.html)<br>

### Backtrace

Display backtrace

```sh
# note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
$ RUST_BACKTRACE=1 cargo run
```

## Unrecoverable errors

Unrecoverable errors with `panic!` macro

```rs
panic!("Panic!");
```

## Recoverable errors

Recoverable errors with `Result`

```rs
enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

### Match errors

`match` expression

```rs
let file = match file_result {
    Ok(file) => file,
    Err(error) => panic!("Problem with file: {:?}", error),
};
```

`match` error kinds

```rs
use std::io::ErrorKind;

let file = match file_result {
    Ok(file) => file,
    Err(error) => match error.kind() {
        ErrorKind::NotFound => match File::create("file.txt") {
            Ok(fc) => fc,
            Err(e) => panic!("File not found: {:?}", e),
        },
        other_error => {
            panic!("Problem opening the file: {:?}", other_error);
        }
    },
};
```

### Closures

Helper methods for `Result<T, E>` type

#### `unwrap_or_else`

```rs
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let file = File::open("file.txt").unwrap_or_else(|error| {
        if error.kind() == ErrorKind::NotFound {
            File::create("file.txt").unwrap_or_else(|error| {
                panic!("Problem creating the file: {:?}", error);
            })
        } else {
            panic!("Problem opening the file: {:?}", error);
        }
    });
}
```

#### `unwrap`

Call `panic!` without error message

```rs
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt").unwrap();
}
```

#### `expect`

Call `panic!` with custom error message

```rs
use std::fs::File;

fn main() {
    let greeting_file = File::open("hello.txt")
        .expect("hello.txt should be included in this project");
}
```

---
### Propagating Errors

```rs
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let username_file_result = File::open("hello.txt");

    let mut username_file = match username_file_result {
        Ok(file) => file,
        Err(e) => return Err(e),
    };

    let mut username = String::new();

    match username_file.read_to_string(&mut username) {
        Ok(_) => Ok(username),
        Err(e) => Err(e),
    }
}
```

#### ? operator

```rs
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut username_file = File::open("hello.txt")?;
    let mut username = String::new();
    username_file.read_to_string(&mut username)?;
    Ok(username)
}
```
