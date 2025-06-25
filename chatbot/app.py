"""Flask application exposing a simple UPSC chatbot API."""

from flask import Flask, jsonify, request

from .knowledge_base import kb

app = Flask(__name__)


@app.route("/ping")
def ping():
    return jsonify({"status": "ok"})


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}
    message = data.get("message", "")
    answer = kb.search(message)
    return jsonify({"answer": answer})


if __name__ == "__main__":
    app.run(debug=True)
