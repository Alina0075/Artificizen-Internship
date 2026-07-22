chat_history = []
def add_to_history(role, content):
    chat_history.append({"role": role, "content": content})
    if len(chat_history)>6:
        del chat_history[:12]

def chat_history_fun():
    return chat_history