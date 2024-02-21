from io import StringIO
from typing import List
from ordered_set import OrderedSet
from dataclasses import dataclass

ASSISTANT = "ASSISTANT"
USER = "USER"
SYSTEM = "SYSTEM"
roles = [ASSISTANT, USER, SYSTEM]

MESSAGE_SEPERATOR = "//----- seperator -----"
FILES_SECTION_START = "## Files section"
CHAT_SECTION_START = "## Chat Section"


@dataclass
class Message:
    def __init__(self, role, content) -> None:
        if role not in roles:
            raise ValueError(f"illegal role {role}")
        self.role = role
        self.content = content

    def __str__(self):
        return f"{self.role}: {self.content}"

    @staticmethod
    def from_str(txt: str):
        for role in roles:
            if txt.startswith(role + ": "):
                return Message(role, txt[len(role + ": "):])

        raise ValueError(f"unkown role in {txt}")


@dataclass
class ConvesationState:
    """
    This class should hold every statefulness of the server,
    Which mainly includes the chat history.
    """

    def __init__(self):
        self.messages: List[Message] = []
        self.files: OrderedSet[str] = OrderedSet()

    def add_msg(self, sender: str, content: str):
        self.messages.append(Message(sender, content))

    def add_file(self, file):
        if self.files.count(file) == 0:
            self.files.add(file)

    def drop_file(self, file):
        self.files.remove(file)

    def __str__(self):
        """Serialize conversation into readable markdown format"""
        f = StringIO("")
        f.write("# Conversation with AI\n\n")
        f.write(FILES_SECTION_START + "\n")
        for file in self.files:
            f.write(file + "\n")
        f.write("\n")

        f.write(CHAT_SECTION_START + "\n")
        msg_str = [str(msg) for msg in self.messages]
        f.write(f"\n\n{MESSAGE_SEPERATOR}\n\n".join(msg_str))
        return f.getvalue()

    @staticmethod
    def from_str(txt: str):
        """Deserialize conversation from markdown format"""
        conversation_state = ConvesationState()
        txt = txt.splitlines()
        i = 0
        while txt[i] != FILES_SECTION_START:
            i += 1
        i += 1

        while txt[i] != CHAT_SECTION_START:
            fname = txt[i].strip()
            if fname:
                conversation_state.add_file(fname)
            i += 1
        i += 1

        chat_section = "\n".join(txt[i:])
        msg_strs = chat_section.split(MESSAGE_SEPERATOR)
        msg_strs = [msg_str.strip() for msg_str in msg_strs]
        msgs = [Message.from_str(txt) for txt in msg_strs]
        conversation_state.messages = msgs
        return conversation_state

    def get_files_content(self):
        pass
