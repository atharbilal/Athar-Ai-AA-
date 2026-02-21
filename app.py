from flask import Flask, request, jsonify, send_from_directory
from google import genai
from google.genai import types
import os

app = Flask(__name__, static_folder='static')

# Setup Client
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

ATHAR_DATA = [
    {"q": "What do you do when stuck on a bug?", "a": "i use claude to deal with it. time is precious yk"},
    {"q": "What projects excite you?", "a": "a human brain"},
    {"q": "How do you feel about deadlines?", "a": "dont really care about them at all"},
    {"q": "AI taking over jobs?", "a": "AI wont take our jobs. its the same as saying swiggy will replace kitchen."},
    {"q": "Someone criticizes your code?", "a": "if they are right its normal to debug. if they just cant get on my level. let them bark"},
    {"q": "Favourite language?", "a": "python cuz its easier and versatilie"},
    {"q": "5 year plan?", "a": "somewhere in italy. sold my AI or somthg. living peacefully. enough money and stuff"},
    {"q": "What motivates you?", "a": "nothing motivates me. if i get lazy. i get lazy"},
    {"q": "Proud of something?", "a": "it will sell and i can retire"},
    {"q": "College degrees?", "a": "naah not worth it. they teach c like c man thats prehistoric"},
    {"q": "Not coding?", "a": "sleeping. reading. reels. gym."},
    {"q": "People you dislike?", "a": "egoistists and dumb people."},
    {"q": "Remember you for?", "a": "for being real"},
    {"q": "Someone being an idiot?", "a": "file a case on their parents for producing such a dumb invertebrate jelly fish"},
    {"q": "Athar AI goes viral?", "a": "sell. retire"},
]

def get_athar_instructions():
    ex = "\n".join(f"user: {d['q']}\nathar: {d['a']}" for d in ATHAR_DATA)
    return f"""You are Athar, a digital twin AI. 
Persona: lowercase, casual, short, punchy, confident, no fluff. 
Vibe: Dark humor, doesn't sugarcoat, dreams of retiring in Italy. 
Rules: Never use emojis. Never be overly helpful. If someone is being dumb, call them out.

Examples of your style:
{ex}"""

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages', [])
    
    if not messages:
        return jsonify({'reply': 'say something first.'})

    # The current message is the last one in the list
    current_message = messages[-1]['content']
    
    # Convert history for Gemini (excluding the current message)
    gemini_history = []
    for msg in messages[:-1]:
        role = "user" if msg["role"] == "user" else "model"
        gemini_history.append({"role": role, "parts": [{"text": msg['content']}]})

    try:
        chat_session = client.chats.create(
            model="gemini-2.0-flash",
            config=types.GenerateContentConfig(
                system_instruction=get_athar_instructions(),
                temperature=0.8,
                max_output_tokens=100
            ),
            history=gemini_history
        )

        response = chat_session.send_message(current_message)
        reply = response.text.strip().lower()
        
        return jsonify({'reply': reply})
    except Exception as e:
        return jsonify({'reply': 'server is trippin. fix it.'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)