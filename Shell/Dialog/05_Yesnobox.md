## Yesnobox

Yes/No question box

## Synopsis

```sh
dialog <title> --yesno <message> <height> <width>
```

**--defaultno**

Make "NO" the default value of the yes/no box.

**Example**

```sh
dialog --title "Title" --defaultno --yesno "Displayed message content" 8 40
```

## Evaluation

The best option is to evaluate the result based on the exit status.

```sh
case $? in
    0)
      echo "YES pressed."
    ;;
    1)
      echo "NO pressed."
    ;;
    255)
      echo "ESC pressed."
    ;;
    *)
      echo "Exit status $?"
      # In theory, this shouldn't happen
    ;;
esac
```
