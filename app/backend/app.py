from flask import Flask, request, jsonify, render_template
import os
import requests
import json

app = Flask(__name__, static_folder="static", template_folder="templates")

# Variáveis de ambiente
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_DEPLOYMENT = os.getenv("AZURE_DEPLOYMENT")

# Página principal
@app.route("/")
def index():
    return render_template("index.html")

# Endpoint para o chat
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("question")

    # Carrega os dados do cliente (chat-1.json)
    with open("app/backend/chat-1.json", encoding="utf-8") as f:
        chat_data = json.load(f)

    # Atualiza a pergunta do usuário no objeto
    chat_data["question"] = user_input
    customer = chat_data["customer"]

    # Constrói o prompt a partir do .prompty manualmente
    prompt = f"""You are an AI agent for the Contoso Outdoors products retailer. 
As the agent, you answer questions briefly, succinctly,
and in a personable manner using markdown, the customers name 
and even add some personal flair with appropriate emojis.

# Documentation
Make sure to reference any documentation used in the response.

# Previous Orders
Use their orders as context to the question they are asking.
"""
    for item in customer.get("orders", []):
        prompt += f"- name: {item['name']}\n  description: {item['description']}\n"

    prompt += f"""

# Customer Context
The customer's name is {customer['firstName']} {customer['lastName']} and is {customer['age']} years old.
{customer['firstName']} {customer['lastName']} has a \"{customer['membership']}\" membership status.

# user
{chat_data['question']}
"""

    # Chamada para Azure OpenAI
    response = requests.post(
        f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{AZURE_DEPLOYMENT}/chat/completions?api-version=2023-12-01-preview",
        headers={
            "Content-Type": "application/json",
            "api-key": AZURE_OPENAI_KEY
        },
        json={
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": ""}
            ],
            "max_tokens": 500,
            "temperature": 0.7
        }
    )

    return jsonify(response.json())

# Executa o app localmente (útil para testes)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
