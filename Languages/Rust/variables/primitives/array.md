# Arrays

[Rust By Example - Arrays and Slices](https://doc.rust-lang.org/rust-by-example/primitives/array.html)<br>
[Rust - array](https://doc.rust-lang.org/std/primitive.array.html)<br>

- **Sequence:** Fixed-size
- **Memory allocation:** Stack
- **Data types:** Same type
- **Indexing syntax:** `.` operator

## Declare

```rs
// Repeat expression [expr; N]
let byte [u8; 8] = [0; 8]; 

// List with each element [x, y, z]
let byte: [u8; 8] = [0, 1, 2, 3, 4, 5, 6, 7];
```

## Methods

```rs
let error_codes = [200, 404, 500];

// Indexing (starts at 0)
let not_found = error_codes[1];

// Access by slice
let not_found = error_codes[0..1];

// Length
error_codes.len();
```
