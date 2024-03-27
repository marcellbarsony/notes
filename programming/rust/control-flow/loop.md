# Loop

## Loop

```rs
let mut counter: i32 = 0;

let result = loop {
    counter += 1;
    if counter == 10 {
        // Break loop & return counter
        break counter;
    }
};
```

## While loop

```rs
let mut counter: i32 = 5;

while number != 0 {
    println!("{}!", number);

    number -= 1;
}
```

## For loop

```rs
for number in 1..10 {
    println!("Number: {}", number);
}
```
