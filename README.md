<<<<<<< HEAD
# TextGenie
=======
# 🤖 AI Chatbot (Generative AI Project)

A conversational AI chatbot built with **Python**, **Streamlit**, and the **Groq API**
(free tier — no payment needed). It answers questions, holds a conversation with
memory, and lets you tune model behavior live.

## ✨ Features
- Chat UI with message bubbles (`st.chat_message`)
- Conversation memory (full history sent to the model each turn)
- Model selector (Llama 3.3 70B / Llama 3.1 8B / Gemma2 9B — all free on Groq)
- Temperature & max-token controls
- Clear chat + download conversation as JSON
- API key entered securely (sidebar input or `.env` file)
- **Mock mode** — test the whole UI/memory flow with canned responses, no API key needed

## 📂 Project Structure
```
ai-chatbot/
├── app.py                 # Streamlit UI
├── chatbot.py              # API call logic (the "brain")
├── prompts/
│   └── system_prompt.txt   # Editable persona/instructions
├── requirements.txt
├── .env.example
└── README.md
```

## 🚀 Setup

1. **Clone / download this folder**, then move into it:
   ```bash
   cd ai-chatbot
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your free Groq API key.**
   Copy `.env.example` to `.env` and paste your key:
   ```bash
   cp .env.example .env
   ```
   ```
   API_KEY=gsk_xxxxxxxx
   ```
   Get a **free** key from https://console.groq.com/keys (sign up with Google/GitHub,
   no credit card required). Groq's free tier gives generous daily request limits.
   (You can also just paste the key into the sidebar at runtime instead.)

4. **Run the app:**
   ```bash
   streamlit run app.py
   ```
   It will open at `http://localhost:8501`.

## 🧪 Don't have a key yet? Use Mock mode

Flip the **"Mock mode"** toggle in the sidebar to try the app without any API key.
You'll get canned responses that still echo your message and turn count — enough
to verify the chat UI, memory, clear/download buttons all work. Turn it off once
you've grabbed your free Groq key to get real LLM responses.

## 🎛️ How it works

- **Memory:** every message (yours and the bot's) is stored in `st.session_state.messages`
  and the *entire* list is sent back to the model on each new question — that's what lets
  it remember earlier parts of the conversation.
- **System prompt:** edit `prompts/system_prompt.txt` to change the bot's personality or
  instructions without touching any code.
- **Temperature:** lower = more consistent/focused answers, higher = more creative/varied.

## 🧩 Ideas to extend (mini challenge)
- [ ] Add voice input/output (`speech_recognition` + `pyttsx3` or a TTS API)
- [ ] Add PDF upload + Q&A (RAG) over the document
- [ ] Persist chat history in a database (SQLite/Postgres) instead of session memory
- [ ] Add a second LLM provider (OpenAI, etc.) behind the same model selector
- [ ] Add a web-search tool so the bot can look up current info

## ☁️ Deployment
Works as-is on:
- **Streamlit Community Cloud** — connect your GitHub repo, set `API_KEY` in the app's Secrets.
- **Hugging Face Spaces** — choose the Streamlit SDK, add `API_KEY` as a Space secret.
- **Render** — set the start command to `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`.

## 💼 Resume blurb
> Developed a conversational AI chatbot using Large Language Models, Python, and Streamlit.
> Implemented prompt engineering, conversation memory, API integration, and an interactive
> UI for intelligent question-answering and contextual conversations.
>>>>>>> 3a04fd0 (Update .env.example, requirements.txt, and README for Groq setup)
