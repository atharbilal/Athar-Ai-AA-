# Athar — The Digital Twin

A local AI mirror built to think, talk, and react exactly like I do. This isn't a generic chatbot; it’s a digital twin that understands the "matchbox" college life, the Japan exit plan, and the "invertebrate jellyfish" that make life dull.

## 🧠 Core Philosophy

The "Athar" model operates on a few-shot personality engine. It doesn't just answer questions—it mimics my specific psychological edge:
- **the dread:** total disgust for the NIT Srinagar environment.
- **the exit:** laser-focused on financial independence and moving to Italy/Japan.
- **the logic:** show don't tell. work in bursts. use AI to debug because time is precious.
- **the vibe:** lowercase only, no emojis, dry humor, and zero patience for egoists.

## 🛠 Tech Stack

- **AI Engine:** [Ollama](https://ollama.com/) running `llama3.2` locally (100% private, no API keys).
- **Backend:** Python + Flask.
- **Frontend:** Minimalist Dark Mode UI with Neon Green accents.
- **Context:** Hardcoded personality core and life-lore integrated directly into the prompt.


# Clone the repository
git clone [https://github.com/atharbilal/athar.git](https://github.com/atharbilal/athar.git)
cd athar

# Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install flask requests
python app.py
athar/
├── app.py             # The Entire Brain (Personality Logic + Server)
├── static/
│   └── index.html     # The UI (Dark/Neon)
└── README.md          # Documentation
*What’s the move now? Should I show you how to add a "Chat Log" feature so you can review what your digital twin says while you're asleep?**
