# Structs

[Structs - Rust By Example](https://doc.rust-lang.org/stable/rust-by-example/custom_types/structs.html)<br>

Structs are a fundamental building block for creating custom data types<br>
Structs are used to group related data together

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
struct ThreeNums(i32, i32, i32);

// Unit struct
struct Calculator;
```

## Accessing fields

Struct fields can be accessed using the `.` notation

```rs
let name = person.name;
```

## Struct Implementation

Implementing methods and associated functions

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

## Function constructors

Constructors are creating objects (new struct instances) with the desired initial state

```rs
let user1 = create_user(
    email: String::from("mail@domain.com"),
    username: String::from("Testuser01")
)

fn create_user(email: String, username: String) -> User {
    User {
        email: email,
        username, // Field init shorthand syntax
        active: true, // Default value
        sign_in_count: 1, // Default value
    }
}
```
