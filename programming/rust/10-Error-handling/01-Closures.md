# Closures

Helper methods for [Result<T, E>](https://doc.rust-lang.org/std/result/) type

<!-- unwrap_or_else {{{-->
## `unwrap_or_else`

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
<!-- }}} -->

<!-- unwrap {{{-->
## `unwrap`

Call `panic!` without error message

```rs
use std::fs::File;

fn main() {
    let greeting_file = File::open("file.txt").unwrap();
}
```
<!-- }}}-->

<!-- expect {{{-->
## `expect`

Call `panic!` with custom error message

```rs
use std::fs::File;

fn main() {
    let greeting_file = File::open("file.txt")
        .expect("file.txt should be included in this project");
}
```
<!-- }}} -->
