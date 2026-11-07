"""
app.py
------
Streamlit front-end for the AI Chatbot.
Run with:  streamlit run app.py
"""

import os
import json
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv

from chatbot import get_client, generate_response, generate_mock_response, load_system_prompt

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------
load_dotenv()

st.set_page_config(page_title="AI Chatbot", page_icon="🤖", layout="centered")

MODEL_OPTIONS = {
    "Llama 3.3 70B (balanced, capable)": "llama-3.3-70b-versatile",
    "Llama 3.1 8B (fastest)": "llama-3.1-8b-instant",
    "Gemma2 9B (Google, lightweight)": "gemma2-9b-it",
}

# ---------------------------------------------------------------------------
# Sidebar settings (Step 11: sidebar settings, clear chat, download)
# ---------------------------------------------------------------------------
with st.sidebar:
    st.header("⚙️ Settings")

    mock_mode = st.toggle(
        "🧪 Mock mode (no API calls)",
        value=False,
        help="Test the chat UI and memory with canned responses — no API key "
             "or credits needed. Turn off once you're ready for real answers.",
    )

    if mock_mode:
        st.info("Mock mode is ON — responses are simulated, not from the real LLM.")

    api_key_input = st.text_input(
        "Groq API Key",
        value=os.getenv("API_KEY", ""),
        type="password",
        help="Free key from console.groq.com/keys — or set API_KEY in a .env file.",
        disabled=mock_mode,
    )

    model_label = st.selectbox("Model", list(MODEL_OPTIONS.keys()), disabled=mock_mode)
    model = MODEL_OPTIONS[model_label]

    temperature = st.slider(
        "Temperature (creativity)", 0.0, 1.0, 0.7, 0.1,
        help="Low = focused & consistent. High = more varied & creative.",
    )
    max_tokens = st.slider(
        "Max response length (tokens)", 100, 2048, 1024, 100,
    )

    st.divider()

    if st.button("🗑️ Clear chat"):
        st.session_state.messages = []
        st.rerun()

    if st.session_state.get("messages"):
        chat_export = json.dumps(st.session_state.messages, indent=2)
        st.download_button(
            "⬇️ Download conversation",
            data=chat_export,
            file_name=f"chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
            mime="application/json",
        )

    st.divider()
    st.caption("Built from the AI Chatbot Generative AI project template.")

# ---------------------------------------------------------------------------
# Main chat UI
# ---------------------------------------------------------------------------
st.title("🤖 AI Chatbot")
st.caption("Ask anything — I remember our conversation as we go.")

# Step 7: Conversation memory lives in session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Render existing chat bubbles
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Chat input
question = st.chat_input("Ask anything...")

if question:
    if not mock_mode and not api_key_input:
        st.error("Please enter your API key in the sidebar (or set it in a .env file), "
                 "or turn on Mock mode to test without one.")
        st.stop()

    # 1. Show user message immediately
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    # 2. Call the model with FULL history (this is what gives it memory)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            if mock_mode:
                reply = generate_mock_response(st.session_state.messages)
            else:
                try:
                    client = get_client(api_key_input)
                    reply = generate_response(
                        client=client,
                        messages=st.session_state.messages,
                        model=model,
                        temperature=temperature,
                        max_tokens=max_tokens,
                    )
                except Exception as e:
                    reply = f"⚠️ Something went wrong calling the API: {e}"
        st.markdown(reply)

    # 3. Save assistant reply to memory too
    st.session_state.messages.append({"role": "assistant", "content": reply})
