# 🧞 TextGenie
 
**TextGenie** is a conversational AI chatbot built with **Python**, **Streamlit**, and the **Groq API** (free tier, no payment required). It answers questions, remembers the conversation, and lets you tune the model's behavior live from the sidebar.
 
---
 
## ✨ Features
 
- 💬 **Chat UI** with message bubbles (`st.chat_message`)
- 🧠 **Conversation memory**: the full history is sent to the model on every turn
- 🔀 **Model selector**: Llama 3.3 70B, Llama 3.1 8B, or Gemma2 9B (all free on Groq)
- 🎛️ **Adjustable settings**: temperature (creativity) and max response length (tokens)
- 🗑️ **Clear chat** and ⬇️ **download conversation as JSON**
- 🔐 **Secure API key handling**: enter it in the sidebar or load it from a `.env` file
- 🧪 **Mock mode**: test the whole UI and memory flow with canned responses, no API key needed
- ✏️ **Editable persona**: change the bot's personality via a plain text system prompt
---
 
## 📂 Project Structure
 
```
TextGenie/
├── app.py                  # Streamlit UI (sidebar, chat display, controls)
├── chatbot.py              # LLM logic: Groq client, response generation, mock mode
├── prompts/
│   └── system_prompt.txt   # Editable system prompt / persona
├── requirements.txt        # Python dependencies
├── .env.example            # Template for environment variables
├── .gitignore
└── README.md
```
 
---
 
## 🛠️ Tech Stack
 
| Component | Technology |
|-----------|------------|
| Language | Python 3.10+ |
| UI | [Streamlit](https://streamlit.io/) |
| LLM provider | [Groq API](https://console.groq.com/) |
| Config | `python-dotenv` |
 
---
 
## 🚀 Getting Started
 
### 1. Clone the repository
 
```bash
git clone https://github.com/ksusmitha879-cyber/TextGenie.git
cd TextGenie
```
 
### 2. (Recommended) Create a virtual environment
 
```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```
 
### 3. Install dependencies
 
```bash
pip install -r requirements.txt
```
 
### 4. Add your Groq API key
 
Get a **free** key at <https://console.groq.com/keys> (sign in with Google or GitHub, no credit card needed).
 
Copy the example env file and add your key:
 
```bash
cp .env.example .env
```
 
Then edit `.env`:
 
```
API_KEY=gsk_your_groq_api_key_here
```
 
> You can also skip this step and paste the key into the app's sidebar at runtime.
 
### 5. Run the app
 
```bash
streamlit run app.py
```
 
The app opens at **http://localhost:8501**.
 
---
 
## 🧪 No API key yet? Use Mock Mode
 
Turn on the **"Mock mode"** toggle in the sidebar to try TextGenie without any key. You'll get simulated replies that echo your message and show the turn count, which is enough to verify the chat UI, memory, and the clear/download buttons. Switch it off once you have a Groq key to get real LLM responses.
 
---
 
## ⚙️ How It Works
 
- **Memory:** every user and assistant message is stored in `st.session_state.messages`, and the whole list is sent to the model with each new question, which lets it remember earlier parts of the conversation.
- **System prompt:** edit `prompts/system_prompt.txt` to change the bot's tone or instructions without touching any code.
- **Temperature:** lower values give focused, consistent answers; higher values give more creative, varied ones.
- **Separation of concerns:** `app.py` handles the interface, while `chatbot.py` handles the API calls, so the "brain" can be tested or reused independently.
---
 
## 🎛️ Available Models
 
| Label in app | Groq model ID |
|--------------|---------------|
| Llama 3.3 70B (balanced, capable) | `llama-3.3-70b-versatile` |
| Llama 3.1 8B (fastest) | `llama-3.1-8b-instant` |
| Gemma2 9B (Google, lightweight) | `gemma2-9b-it` |
 
> Groq's model lineup changes over time. If a model is unavailable, update `MODEL_OPTIONS` in `app.py` using the current list at <https://console.groq.com/docs/models>.
 
---
 
## ☁️ Deployment
 
TextGenie works as-is on:
 
- **Streamlit Community Cloud**: connect your GitHub repo and add `API_KEY` in the app's Secrets.
- **Hugging Face Spaces**: choose the Streamlit SDK and add `API_KEY` as a Space secret.
- **Render**: use the start command
  `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
---
 
## 🧩 Ideas for Future Improvements
 
- [ ] Voice input/output (`speech_recognition` + `pyttsx3` or a TTS API)
- [ ] PDF upload with Q&A (RAG) over the document
- [ ] Persistent chat history in a database (SQLite/Postgres)
- [ ] Support for additional LLM providers behind the same model selector
- [ ] Web-search tool for up-to-date information
- [ ] Streaming responses
---
 
## 🔒 Security Notes
 
- Never commit your `.env` file. It is already listed in `.gitignore`.
- Keep your API key private; rotate it from the Groq console if it is ever exposed.
---
 
## 🤝 Contributing
 
Contributions, issues, and feature requests are welcome. Fork the repo, create a feature branch, and open a pull request.
 
---
 
## 📄 License
 
No license has been specified yet. Consider adding one (for example, MIT) via a `LICENSE` file.
 
---
 
## 👤 Author
 
**ksusmitha879-cyber**
GitHub: [@ksusmitha879-cyber](https://github.com/ksusmitha879-cyber)
