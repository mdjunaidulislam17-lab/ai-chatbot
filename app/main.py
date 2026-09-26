from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.models import ChatRequest
from app.memory import get_history, add_message
from app.chatbot import generate_response


app = FastAPI(title="AI Chatbot API")


# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)


@app.get("/")
def home():
    return {
        "message": "AI Chatbot API is running"
    }


@app.post("/chat")
def chat(request: ChatRequest):

    try:
        # Get conversation history
        history = get_history(request.session_id)

        # Generate AI response
        answer = generate_response(
            request.message,
            history
        )

        # Save conversation
        add_message(
            request.session_id,
            request.message,
            answer
        )

        return {
            "session_id": request.session_id,
            "user_message": request.message,
            "answer": answer
        }

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="AI service is currently unavailable. Please try again later."
        )