## GitHub code syntax highlighting

GitHub is using [Linguist](https://github.com/github/linguist) to perform language detection and to select [third-party grammars](https://github.com/github/linguist/blob/master/vendor/README.md) for syntax highlighting.

## Keywords

- **Shell:** console, shell
- **Bash:** bash, sh, zsh
- **PowerShell:** powershell, ps
- **DOS:** dos, bat, cmd

Highlight the first word as a command with `properties`:

```properties
npm run build
```

Highlight shell session command sequence with `console`:

```console
foo@bar:~$ whoami
foo
```

Complete [keyword list](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml)

[[GitHub Docs](https://docs.github.com/en/github/writing-on-github/working-with-advanced-formatting/creating-and-highlighting-code-blocks)]

[[Markdown guide](https://www.markdownguide.org/extended-syntax/)]
