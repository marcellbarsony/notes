# Open a file

```sh
use std::fs::File;

fn main() {
    let f = File::open("file.txt").unwrap();
}
```
