import unittest
from aitoolbox.server.state import ConvesationState, Message


class TestPrinterParser(unittest.TestCase):
    def testMsg(self):
        msg = Message("ASSISTANT", "\ncontent:\n\nhiiii\n")
        self.assertEqual(msg, Message.from_str(str(msg)))

    def testConversation(self):
        conversation = ConvesationState()
        conversation.add_file("/tmp/tmp2.txt")
        conversation.add_file("/tmp/tmp1.txt")
        conversation.add_msg("SYSTEM", "you are an helpful bot")
        conversation.add_msg("USER", "hi bot!")
        conversation.add_msg("ASSISTANT", "hi user! how can I help you?")
        with open("/tmp/tmp.md", "w") as f:
            f.write(str(conversation))
        self.assertEqual(conversation, ConvesationState.from_str(str(conversation)))


if __name__ == "__main__":
    unittest.main()
