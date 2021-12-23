# Variables

## Valid syntax

```sh
VARIABLE_NAME="Value"
```

```sh
FIRST3LETTERS="ABC"
FIRST_THREE_LETTERS="ABC"
firstThreeLetters="ABC"
_FIRST3LETTERS="ABC"
```

Example

```sh
MY_SHELL="bash"
echo "I like the $VARIABLE_NAME shell"
echo "I like the ${VARIABLE_NAME} shell"
```

## Invalid syntax

```sh
3LETTERS="ABC"
first-three-letters="ABC"
first@Three@Letters="ABC"
```

## Command output to a variable

```sh
SERVER_NAME=$(hostname)
echo "This script is running on ${SERVER_NAME}."
```