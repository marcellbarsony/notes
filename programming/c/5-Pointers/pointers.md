# Pointers

```c
int n = 10;                                 // declaration + initialization
int *pointer = &n;                          // &: Address of n (8 bytes/64 bits)
printf("Address of n: %p\n", pointer);      // Show the address
printf("Value of n: %i\n", *pointer);       // Get the value (dereference)
printf("Address of abc[1]: %p\n", &abc[1]); // Get the address of abc[1]
```
