import os
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Tumhara Green light wala Space URL
HF_BRAIN_URL = "https://lalubhai-rex.hf.space/ask" 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    user_text = request.json.get("message")
    try:
        # Timeout 60 second rakha hai taaki browser load ho sake
        response = requests.post(HF_BRAIN_URL, json={"message": user_text}, timeout=120)
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"reply": f"REX ke dimaag se sampark nahi ho paya. Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
    
