# Math

## Arithmetic operators

```c
x + y // Addition
x – y // Subtraction
x * y // Multiplication
x / y // Division
x % y // Modulus
```

## Augmented assignment operators

```c
x+=1; // x = x + 1;
x-=1; // x = x - 1;
x*=1; // x = x * 1;
x/=1; // x = x / 1;
x%=1; // x = x % 1;
```

## Math functions

```c
double A = sqrt(9);
double B = pow(2, 4);
int C = round(3.14);
int D = ceil(3.14);
int E = floor(3.14);
double F = fabs(-100);
double G = log(3);
double H = sin(45);
double I = cos(45);
double J = tan(45);
```

## Ternary operators

Ternary operators are expressions whose value depends on the result of a
conditional embedded in it.
```c
// If x > 10, add 17 to y. Otherwise add 37 to y.
y += x > 10? 17: 37;

if (x > 10)
    y += 17;
else
    y += 37;
```
