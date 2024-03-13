from aitoolbox.server.state import ConvesationState


def state2openai(state: ConvesationState):
    # return the conversation history in openai messages formet, without files.
    # use basic "you are an helpful chatbot" prompt.
    messages = []
    messages.append(
        {"role": "system", "content": "you are an helpful chatbot"})
    for msg in state.messages:
        messages.append({"role": msg.role, "content": msg.content})

    return messages
