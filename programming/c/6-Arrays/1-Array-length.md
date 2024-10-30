# Arrays

An array in C is a collection of elements, all of the same data type, stored in
contiguous memory locations.

- **Homogeneous Data**: All elements must be of the same data type.
- **Contiguous Memory**: Elements are stored in consecutive memory locations,
  making access fast.
- **Fixed in size**: Once an array's size is defined, it cannot be changed.
- **Zero-Based Indexing**: The first element is at index 0, the second at 1,
  andso on...

- [Beej's Guide to C programming - Arrays](https://beej.us/guide/bgc/html/split-wide/arrays.html#arrays)

## Array declaration

```c
#include <stdio.h>

int main(void)
{
    int i;
    float f[4];  // Declare an array of 4 floats

    f[0] = 3.14159;
    f[1] = 1.41421;
    f[2] = 1.61803;
    f[3] = 2.71828;

    for (i = 0; i < 4; i++) {
        printf("%f\n", f[i]);
    }
}
```

## Array length

- [Beej's Guide to C programming - Getting the Length of an Array](https://beej.us/guide/bgc/html/split-wide/arrays.html#getting-the-length-of-an-array)



## ChatGPT

To declare an array, you specify the type of its elements, the array's name,
and the number of elements it will hold:

type array_name[size];
- type: The data type of elements in the array (e.g., int, float, char).
- array_name: The name of the array.
- size: The number of elements the array can hold.

Example
```c
int numbers[5]; // Declares an array of 5 integers
```

In this example, numbers is an array that can hold 5 integers.

### Initializing an Array

Arrays can be initialized at the time of declaration by specifying values in
braces {}:
```c
int numbers[5] = {1, 2, 3, 4, 5};
```

If the size is omitted, it will automatically be determined by the number of elements:

```c
int numbers[] = {1, 2, 3, 4, 5}; // size is automatically set to 5
```

### Accessing Array Elements

Array elements are accessed using the index number, with indexing starting from 0:
```c
int value = numbers[2]; // Accesses the third element, which is `3` in this example
```

Here's a simple example of how arrays work in C:
```c
#include <stdio.h>

int main() {
    int numbers[5] = {1, 2, 3, 4, 5}; // Declare and initialize an array
    for (int i = 0; i < 5; i++) {
        printf("Element at index %d is %d\n", i, numbers[i]);
    }
    return 0;
}
```

This program will print each element in the numbers array along with its index.
