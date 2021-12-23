# If Statement

## Syntax

```sh
if [ condition-is-true ]
then
    command 1
    command 2
    command N
fi
```

Example

```sh
MY_SHELL="bash"

if [ "$MY_SHELL" = "bash" ]
then
    echo "We're using the bash shell."
fi
```

# If-Else Statement

## Syntax

```sh
if [ condition-is-true ]
then
    command N
else
    command N
fi
```

Example

```sh
MY_SHELL="zsh"

if [ "$MY_SHELL" = "bash" ]
then
    echo "We're using the bash shell."
else
    echo "We're using some other shell."
fi
```

# If-Elif-Else Statement

## Syntax

```sh
if [ condition-is-true ]
then
    command N
elif [ condition-is-true ]
then
    command N
else
    command N
fi
```

Example

```sh
MY_SHELL="zsh"

if [ "$MY_SHELL" = "bash" ]
then
    echo "We're using the bash shell."
elif [ "$MY_SHELL" = "fish" ]
then
    echo "We're using the fish shell."
else
    echo "We're using some other shell."
fi
```
