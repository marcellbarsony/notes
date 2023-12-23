# References and Borrowing

[References and Borrowing - The Rust Book](https://doc.rust-lang.org/book/ch04-02-references-and-borrowing.html)

## Borrowing rules

- No dangling references: A reference must always be valid, which means that the data it refers to must still be alive.
Rust will check the scopes of references to ensure that this is true.

- No two mutable borrows: At any given time, there can only be one mutable borrow of a particular piece of data.
This prevents data races, which can occur when multiple threads try to modify the same data at the same time.

- Multiple immutable borrows: There can be any number of immutable borrows of a particular piece of data at the same time.
This allows multiple threads to read the value of the data without any risk of data races.

## Rules of references

Let’s recap what we’ve discussed about references:

- At any given time, you can have either one mutable reference or any number of immutable references.

- References must always be valid.

# Exclusive (Mutable)
# Shared (Immutable)
