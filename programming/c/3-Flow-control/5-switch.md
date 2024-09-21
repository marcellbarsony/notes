# Switch statement

```c
int count = 2;

switch (count) {
    case 0:
        printf("Count is 0\n");
        break;
    case 1:
        printf("Count is 1\n");
        break;
    case 2:
        printf("Count is 2\n");
        break;
    default:
        printf("Default value\n");
        break;
}
```
Switch statements accept `int` and `char` types only.

## Fall through

If we don't `break` out of switch we are falling through.

```c
int i = 1;

switch (i) {
    case 1:
        printf("1\n");
        // Fall through
    case 2:
        printf("2\n");
        break;
    case 3:
        printf("3\n");
        break;
}
```
If `i == 1`, this `switch` will first hit `case 1`, it'll print `1` and continues to the
next line of code.
