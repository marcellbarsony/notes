# Create directory

Create a new, empty directory

```rs
use std::fs;

fn main() -> std::io::Result<()> {
    fs::create_dir("/some/dir")?;
    Ok(())
}
```

## Errors

This function will return an error if

- The user lacks persmission
- The parent of the given path doesn't exists
- The path already exists
