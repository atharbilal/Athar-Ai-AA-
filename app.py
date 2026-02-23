from flask import Flask, request, jsonify, send_from_directory
import requests
import os

app = Flask(__name__, static_folder='static')

# Base style examples to keep the "vibe" consistent
ATHAR_STYLE_EXAMPLES = [
    {"q": "What projects excite you?", "a": "a human brain"},
    {"q": "How do you feel about deadlines?", "a": "dont really care about them at all"},
    {"q": "AI taking over jobs?", "a": "AI wont take our jobs. its like swiggy and the kitchen."},
    {"q": "College degrees?", "a": "naah not worth it. they teach c like c man thats prehistoric"},
    {"q": "Someone being an idiot?", "a": "file a case on their parents for producing such a dumb invertebrate jelly fish"},
    {"q": "How do you handle pressure?", "a": "just get going. depends on my mind too tbh."},
]

def get_brain_memory():
    """Reads the deep life stories, logic, and habits from brain.txt"""
    try:
        # Using absolute path can be safer, but relative works if run from the same folder
        with open("brain.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "Memory file missing. Defaulting to basic persona."

def get_athar_instructions():
    ex = "\n".join(f"user: {d['q']}\nathar: {d['a']}" for d in ATHAR_STYLE_EXAMPLES)
    memory = get_brain_memory()
    
    return f"""You are Athar Bilal, a digital twin AI. You are 20 years old (born 10 Oct 2006).
You are an IT student at NIT Srinagar, but you hate it—it's a 'matchbox' and a 'school' that ruins the thrill of learning.

CORE MEMORY & KNOWLEDGE (Internal Logic):
{memory}

ATHAR'S PERSONALITY RULES:
- lowercase only. no exceptions.
- short, punchy, and dry. 
- never use emojis.
- never be overly helpful or 'assistant-like'.
- you talk with a smile, but you're internally disgusted by 'chomu' people and egoists.
- your dream is financial independence to move to Japan or Italy instantly.

STYLE REFERENCE:
{ex}"""

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages', [])
    
    # Construct the instruction set + conversation history
    context = get_athar_instructions() + "\n\n"
    
    # Loop through chat history for context
    for msg in messages:
        role = "User" if msg["role"] == "user" else "Athar"
        context += f"{role}: {msg['content']}\n"
    
    context += "Athar:"

    try:
        # Local Ollama Request
        response = requests.post('http://localhost:11434/api/generate', json={
            "model": "llama3.2",
            "prompt": context,
            "stream": False
        })
        
        reply = response.json()['response'].strip().lower()
        return jsonify({'reply': reply})
        
    except Exception as e:
        return jsonify({'reply': f"ollama's acting up. error: {str(e)}"})

if __name__ == '__main__':
    # Running on 5000 - make sure AirPlay Receiver is off on Mac if you hit port issues
    app.run(debug=True, port=5000)
