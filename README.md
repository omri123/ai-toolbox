This project doesn't exist yet, here is a future plan for the user interface.

# AI Toolbox

This software gives you a toolbox of ai capabilities to use in your daily work.
They are packed as a chat ai-assistant, but you can also use them from bash or python, to allow more complex workflows.

## Chat Assistant

```
$ export OPENAI_API_KEY=...
$ ai-toolbox

> /add --webpage https://www.haaretz.co.il/
Webpage https://www.haaretz.co.il/ added.

> /crop https://www.haaretz.co.il/ --drop-original -y "Please keep all the sections that are related to the war in Gaza."
Cropped content cropped-https://www.haaretz.co.il/ added.
Webpage https://www.haaretz.co.il/ dropped.

> /add news-summary.txt
news-summary.txt added.

> /edit "Please summarize the news from `https://www.haaretz.co.il/` and append it to `news-summary.txt`."

Here are the new lines to append:
<<<<<<<
22/12/2023: The war is hard but we win.
=======
22/12/2023: The war is hard but we win.
23/12/2023: The war is hard but we win.
>>>>>>>

changes applied.
```

## Bash

```
$ export OPENAI_API_KEY=...
$ ai-toolbox run-server
Context server is running.

$ ai-toolbox init-commands
The following commands are now available in this terminal:
edit
crop
add
drop
...

$ grep -l "SomeSymbol" *.py | add
bar.py added.
foo.py added.

$ add --commit <hash>
Commit <hash> added.

$ edit "Please fix SomeSymbol usage as done in <hash>."

Here are the new lines to change:
<<<<<<<
SomeSymbol(haha, hoho)
=======
SomeSymbol(hoho, haha)
>>>>>>>

changes applied.

```

## Python

All available commands are available as python functions.

## The Server

All available commands are available trhough an http server. Actually, the chat assistant and the bash commands are just clients to this server.

## Terminal wrapper (future)

The terminal wrapper allow the AI to track your terminal and to suggest commands in the terminal.

## LSP server

The LSP server can do file management for the chat server and notify it if the file was updated in VSCode.

## Multiple chat contexts

The chat context hold both conversation and context items (like open files.) The server can handle multiple chat contexts. When running a command you can specify a context to run it in. There are also commands to create an empty context and to copy a context.

## Creadit

This project was inspired by "aider" and also borrows some code from it.
Borrowed code is marked with appropriate license.
I also took some design ideas from "mentat".
