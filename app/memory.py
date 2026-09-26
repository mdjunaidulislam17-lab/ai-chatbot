conversation_memory = {}


def get_history(session_id: str):
    if session_id not in conversation_memory:
        conversation_memory[session_id] = []

    return conversation_memory[session_id]


def add_message(session_id: str, user_message: str, ai_response: str):
    history = get_history(session_id)

    history.append(
        ("human", user_message)
    )

    history.append(
        ("ai", ai_response)
    )