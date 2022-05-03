# Redirection

## STDIN (0)

Read STDIN from a file

```sh
cat 0< input.txt
```

## STDOUT (1)

Redirect STDOUT to `output.txt`

```sh
cat 1> output.txt
```

## STDERR (2)

Append STDERR to `error.txt`

```sh
cat 2>> error.txt
```

## STDOUT & STDERR

```sh
cat 1>> output.txt 2>> error.txt
```

## STDIN & STDOUT & STDERR

```sh
cat 0< input.txt 1>> output.txt 2>> error.txt
```
