# Structs

## Struct Definition

```rs
// C-style struct
struct Data {
    num1: u8,
    num2: u16,
    str: String,
    opt: Option<i32>
}

// Tuple struct
struct TwoNums(i32, i32);

// Unit struct
struct Calculator;
```

## Struct Implementation

```rs
impl Person {
    // Associated function (Static method)
    fn new_type(string: String, num: u8) -> Type {
        Type { string, num }
    }

    // Method
    fn set_num(&mut self, num: u8) {
        self.num = num;
    }
```
