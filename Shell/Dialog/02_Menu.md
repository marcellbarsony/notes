## Menu

## Synopsis

```sh
dialog --title "Title" --menu "Menu text" <window height> <window widht> <list height> <options> <description> ...
```

**Example**

```sh
result=$(dialog --title "Title" --menu "Select option" 20 78 10 ${options[@]} 3>&1 1>&2 2>&3)
```

## Evaluation

The best option is to save the output to a variable (`$result`) and evaluate the result based on the exit status

```sh
case $? in
    0)
      echo "OK pressed."
      echo "Option selected: $result"
    ;;
    1)
      echo "CANCEL pressed."
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

Presssing the "OK" button returns the value (left column) of the selected menu item.
