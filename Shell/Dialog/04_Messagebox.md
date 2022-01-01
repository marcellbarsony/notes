## Messagebox

Message box stops the program from running and waits for the user to acknowledge the displayed message.

## Synopsis

```sh
dialog <title> --msgbox <message> <height> <width>
```

**Example**

```sh
dialog --title "Title" --msgbox "Displayed message content" 8 40
```

## Evaluation

```sh
if [[ $? == 0 ]] ; then
    echo "OK pressed."
else
    echo "ESC pressed."
fi
```
