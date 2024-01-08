# Tuple

[Rust By Example - Tuples](https://doc.rust-lang.org/rust-by-example/primitives/tuples.html)<br>
[Rust - tuple](https://doc.rust-lang.org/std/primitive.tuple.html)

- **Sequence:** Fixed-size
- **Memory allocation:** Stack or Heap
- **Data types:** Any type (heterogenous)
- **Indexing syntax:** `.` operator

## Declare

```rs
let tup = ("Lorem ipsum", 100_000);
```

## Methods

```rs
// Indexing (starts at 0)
let string = tup.0;
let number = tup.1;

// Destructuring
let (string, number) = tup;
```
