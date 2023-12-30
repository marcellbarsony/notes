# Enums

Enums allow to enumerate a list of variants

```rs
enum IpAddrKind {
    V4(u8, u8, u8, u8),
    V6(String),
}

let localhost_v4 = IpAddrKind::V4(127, 0, 0, 1);
let localhost_v6 = IpAddrKind::V6(String::from("::1"));
```

## Methods

```rs
impl IpAddrKind {
    fn get_localhost() {
        println!("{}", IpAddrKind::V6);
    }
}
```

## Option enum

```rs
enum Option<T> {
    Some(T),
    None
}

let x: Option<i8> = Some(5);
let y: Option<i8> = None;
let sum  = x.unwrap_or(0) + y.unwrap_or(0);
```

## Match expression

## If-let syntax

## Use

[use](https://doc.rust-lang.org/stable/rust-by-example/custom_types/enum/enum_use.html)
