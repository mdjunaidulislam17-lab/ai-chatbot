from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_xai import ChatXAI

load_dotenv()


llm = ChatXAI(
    model="grok-4.7",
    temperature=0
)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """You are a helpful, professional, and friendly AI assistant.

Rules:
- Answer clearly and accurately.
- Keep answers easy to understand.
- If you don't know something, say that you don't know.
- Do not invent information.
"""
    ),
    ("placeholder", "{history}"),
    ("human", "{message}")
])


chain = prompt | llm


def generate_response(message: str, history: list):

    response = chain.invoke({
        "history": history,
        "message": message
    })

    return response.content