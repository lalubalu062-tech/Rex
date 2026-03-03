from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Tumhare Hugging Face Space ka API URL
# Example: https://lalubhai-rex-logic.hf.space/ask
HF_BRAIN_URL = "https://YOUR_USERNAME-YOUR_SPACE_NAME.hf.space/ask"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send', methods=['POST'])
def send_message():
    user_text = request.json.get("message")
    # Brain (HF) ko message bhej rahe hain
    response = requests.post(HF_BRAIN_URL, json={"message": user_text})
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
