# Commands

    msg <options> <content>
    message the AI.

    edit <options> <instruction>
    Ask the AI to edit.
    options can be:
        --auto-commit
        
    cli <options> <instructions>
    Ask the AI to suggest bash command.
    options can be:
        --shell-type
    
    crop <options> <instruction> <text-item>
    Ask the AI to crop the text item according to the instruction and chat history.
    
    filter <options> <instruction> <text-items>
    Ask the AI to filter text items according to the instruction and chat history.
    options can be:
        --sep: seperator, default to `//---`
    
    add [paths]
    Add writeable files to the chat
    
    drop [paths]
    Drop writeable files from the chat
    
    sum <options> <instructions> <content>
    Summarize the content according to the instruction and chat history.
    
    web <options> <url>
    Retrive the content of a webpage and print to terminal.
    Options can be:
        --preserve-links
