from aitoolbox.server.state import ConvesationState


def state2openai(state: ConvesationState, system_msg):
    # return the conversation history in openai messages formet, without files.
    # use basic "you are an helpful chatbot" prompt.
    messages = []
    messages.append(
        {"role": "system", "content": system_msg})
    for msg in state.messages:
        messages.append({"role": msg.role, "content": msg.content})

    return messages
