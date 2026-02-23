# Athar — Digital Twin Chatbot

A personal AI chatbot that mimics my communication style, personality, and opinions. Built with Flask and powered by a local LLM via Ollama — no API keys, no cloud, no quota issues.

## What it does

You talk to it, it responds like me. Lowercase, casual, no fluff, occasionally calls you out if you're being dumb.

## Tech Stack

- **Backend:** Python + Flask
- **AI:** Ollama (llama3.2) running locally
- **Frontend:** HTML/CSS/JS — dark theme, neon green accents

## Setup

### 1. Install Ollama

```bash
brew install ollama
ollama pull llama3.2
ollama serve
```

### 2. Clone and install dependencies

```bash
git clone https://github.com/yourusername/athar.git
cd athar
python -m venv .venv
source .venv/bin/activate
pip install flask requests
```

### 3. Run

```bash
python app.py
```

Open `http://127.0.0.1:5000`

## Project Structure

```
athar/
├── app.py              # Flask backend + personality prompt
├── static/
│   └── index.html      # Frontend UI
└── README.md
```

## How the personality works

`app.py` contains a system prompt with Q&A examples of how I actually talk, plus rules like:
- always lowercase
- never use emojis
- short and punchy responses
- call out dumb questions

The model picks up the style from the examples and stays in character.

## Why local?

Started with Gemini free tier — kept hitting quota limits. Switched to Ollama so it runs fully offline, free, and fast enough on a MacBook.

## Status

Working locally. Deployment coming soon.
