# Tuple

[Rust By Example - Tuples](https://doc.rust-lang.org/rust-by-example/primitives/tuples.html)<br>
[Rust - tuple](https://doc.rust-lang.org/std/primitive.tuple.html)

- **Sequence:** Fixed-size
- **Memory allocation:** Stack or heap
- **Data types:** Any type (heterogenous)
- **Indexing syntax:** `.` operator

## Destructuring

```rs
let tup = ("Lorem ipsum", 100_000);

let (string, number) = tup;

// Destructure by Index
let string = tup.0;
let number = tup.1;
```
