# 🤖 TamerOnline - Google AI Studio (Gemini Chat CLI)

An interactive chat interface using Google's Gemini model, built with Python.  
This project allows you to start a chat session with the Gemini-1.5-Pro model via the terminal after configuring your API key.

---

## 🚀 Features

- Quick connection to Google's Gemini model.
- Real-time interactive chat session.
- Secure loading of environment variables using `.env`.
- Direct experience with Gemini-1.5-Pro model.

---

## 🦾 Requirements

- Python 3.8 or higher
- Google Cloud account with Gemini API enabled
- A valid API key

---

## 📦 Installation

```bash
git clone https://github.com/TamerOnLine/tameronline-goodle_al_studio.git
cd tameronline-goodle_al_studio
pip install -r requirements.txt
```

---

## 🔐 API Key Setup

Create a `.env` file in the project root and add your API key as follows:

```env
GEMINI_API_KEY=your_api_key_here
```

> You can obtain the API key from [Google AI Studio](https://makersuite.google.com/app) after logging in with your Google account and activating the service.

---

## ▶️ Usage

Run the script from the terminal:

```bash
python main.py
```

Start chatting right away!  
Type `exit` to end the session.

---

## 🛠️ Core Files

| File | Description |
|------|-------------|
| `main.py` | Main script containing the chat logic |
| `requirements.txt` | Packages required to run the project |
| `.env` | Environment variables file (not included) |
| `README.md` | This documentation file |

---

## 📌 Notes

- Ensure the API key is valid and has access to the Gemini model.
- In case of connection errors, detailed error messages will be displayed in the terminal.
- This tool is intended for testing and learning purposes, not production use.

---

## 📧 Contact

Project owner: [Tamer OnLine](https://github.com/TamerOnLine)  
For inquiries: info@mystrotamer.com

---

## 🧠 Project Future (Suggestions)

- Graphical interface using Streamlit or Gradio.
- Support for saving and retrieving chat sessions.
- Support for custom commands within the chat.
- Analysis and summarization of model responses.

---

## 📝 License

An open-source project for free use.  
You may modify or build upon it in accordance with Google API terms.

