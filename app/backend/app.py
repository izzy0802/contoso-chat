from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

#from flask import Flask, request, jsonify, send_from_directory
#import os
#import requests

#app = Flask(__name__)

#AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
#AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
#AZURE_DEPLOYMENT = os.getenv("AZURE_DEPLOYMENT")

#@app.route("/chat", methods=["POST"])
#def chat():
#    user_input = request.json.get("question")
    
#    response = requests.post(
#        f"{AZURE_OPENAI_ENDPOINT}/openai/deployments/{AZURE_DEPLOYMENT}/chat/completions?api-version=2023-12-01-preview",
#        headers={
#            "Content-Type": "application/json",
#            "api-key": AZURE_OPENAI_KEY
#        },
#        json={
#            "messages": [
#                {"role": "system", "content": "You are a helpful assistant."},
#                {"role": "user", "content": user_input}
#            ],
#            "max_tokens": 300,
#            "temperature": 0.7
#        }
#    )

#    return jsonify(response.json())

#app = Flask(__name__, static_folder="static")

#@app.route("/")
#def index():
#    return send_from_directory(app.static_folder, "index.html")

#@app.route("/script.js")
#def serve_js():
#    return send_from_directory(app.static_folder, "script.js")

# Run the app
#if __name__ == "__main__":
#    port = int(os.environ.get("PORT", 8000))
#    app.run(host="0.0.0.0", port=port)
