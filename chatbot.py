"""
chatbot.py
----------
Core logic layer for the AI Chatbot.
Handles API calls to the LLM (via Groq's free-tier API), keeping this separate
from the Streamlit UI (app.py) so the "brain" of the bot can be tested or
reused independently.
"""

import os
import random
import time
from groq import Groq

# Load system prompt from file so it's easy to edit without touching code
SYSTEM_PROMPT_PATH = os.path.join(os.path.dirname(__file__), "prompts", "system_prompt.txt")


def load_system_prompt() -> str:
    """Read the system prompt from the prompts/ folder."""
    try:
        with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "You are a helpful AI assistant."


def get_client(api_key: str) -> Groq:
    """Create a Groq API client."""
    return Groq(api_key=api_key)


def generate_response(
    client: Groq,
    messages: list[dict],
    model: str = "llama-3.3-70b-versatile",
    temperature: float = 0.7,
    max_tokens: int = 1024,
    system_prompt: str | None = None,
) -> str:
    """
    Send the full conversation history to the model and return its reply.

    messages: list of {"role": "user"|"assistant", "content": str}
              (this is the "conversation memory" step from the project)
    """
    if system_prompt is None:
        system_prompt = load_system_prompt()

    # Groq's API is OpenAI-compatible: the system prompt goes IN the
    # messages list (unlike Anthropic, which takes it as a separate field).
    full_messages = [{"role": "system", "content": system_prompt}, *messages]

    response = client.chat.completions.create(
        model=model,
        max_tokens=max_tokens,
        temperature=temperature,
        messages=full_messages,
    )

    return response.choices[0].message.content


# ---------------------------------------------------------------------------
# Mock mode
# ---------------------------------------------------------------------------
# Lets you test the UI, conversation memory, and chat flow WITHOUT calling
# the real API — useful before you've added credits, or while offline.

_MOCK_OPENERS = [
    "Here's a mock response so you can test the UI without using real credits.",
    "(Mock mode is on — this isn't a real AI answer.)",
    "Simulating a reply here, since no API call was made.",
]


def generate_mock_response(messages: list[dict]) -> str:
    """
    Return a canned response instead of calling the API.
    Still "reads" the conversation so you can see memory working —
    it echoes back the last user message and how many turns have happened.
    """
    time.sleep(0.6)  # small delay so it feels like it's "thinking"

    last_user_msg = next(
        (m["content"] for m in reversed(messages) if m["role"] == "user"), ""
    )
    turn_count = sum(1 for m in messages if m["role"] == "user")

    opener = random.choice(_MOCK_OPENERS)
    return (
        f"{opener}\n\n"
        f"You said: \"{last_user_msg}\"\n"
        f"This is turn #{turn_count} in our conversation."
    )
