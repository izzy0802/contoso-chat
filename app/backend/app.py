from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_DEPLOYMENT = os.getenv("AZURE_DEPLOYMENT")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("question")
    
    response = requests.post(
        f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{AZURE_DEPLOYMENT}/chat/completions?api-version=2023-12-01-preview",
        headers={
            "Content-Type": "application/json",
            "api-key": AZURE_OPENAI_KEY
        },
        json={
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ],
            "max_tokens": 300,
            "temperature": 0.7
        }
    )

    return jsonify(response.json())
