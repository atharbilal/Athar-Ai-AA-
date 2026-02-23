import os
import requests
from flask import Flask, request, jsonify, send_from_directory

base_dir = os.path.abspath(os.path.dirname(__file__))
static_dir = os.path.join(base_dir, 'static')

app = Flask(__name__, static_folder=static_dir)

# Use the exact name from your 'ollama list'
OLLAMA_ENDPOINT = "http://ollama:11434/api/generate"
MODEL_NAME = "llama3.2:latest" 

@app.route('/')
def index():
    return send_from_directory(static_dir, 'index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get("message", "")

        payload = {
            "model": MODEL_NAME,
            "prompt": user_message,
            "stream": False
        }

        # Increased timeout because first run after pull can be slow
        # Change timeout from 60 to 120
        response = requests.post(OLLAMA_ENDPOINT, json=payload, timeout=120)
        
        if response.status_code != 200:
            return jsonify({"response": f"Ollama error: {response.text}"}), 500
            
        result = response.json()
        ai_text = result.get("response", "I thought of nothing.")
        return jsonify({"response": ai_text})

    except Exception as e:
        # This is where your "idk man" was likely coming from
        return jsonify({"response": f"Server is trippn: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
