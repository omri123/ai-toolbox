from aitoolbox.server.state import ConvesationState


def state2openai(state: ConvesationState, sysmsg1=None, sysmsg2=None):
    # return the conversation history in openai messages formet, without files.
    # use basic "you are an helpful chatbot" prompt.
    messages = []
    if sysmsg1:
        messages.append({"role": "system", "content": sysmsg1})
    for msg in state.messages:
        messages.append({"role": msg.role, "content": msg.content})
    if sysmsg2:
        messages.append({"role": "system", "content": sysmsg2})

    return messages
