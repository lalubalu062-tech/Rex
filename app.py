import os
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Ekdum sahi URL
HF_BRAIN_URL = "https://lalubhai-rex.hf.space/ask" 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    user_text = request.json.get("message")
    try:
        # Hugging Face ko batana padta hai ki hum JSON bhej rahe hain
        response = requests.post(
            HF_BRAIN_URL, 
            json={"message": user_text}, 
            headers={"Content-Type": "application/json"},
            timeout=120
        )
        return jsonify(response.json())
    except Exception as e:
        print(f"ERROR: {str(e)}") # Ye Render ke logs mein dikhega
        return jsonify({"reply": "REX ka dimaag offline hai ya network issue hai."}), 500

if __name__ == "__main__":
    # Render ke liye port 10000 sahi hai
    app.run(host='0.0.0.0', port=10000)
