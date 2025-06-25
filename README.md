# UPSCChatbot

This project implements a minimal prototype of the UPSC Chatbot described in the product requirements document. It exposes a small REST-style API using a lightweight builtin web framework.

## Setup

1. Run the server:
   ```bash
   python -m chatbot.app
   ```

2. Run the tests:
   ```bash
   PYTHONPATH=. pytest -q
   ```

The server provides two endpoints:
- `GET /ping` returns a simple status check.
- `POST /chat` expects JSON `{"message": "your question"}` and returns an answer from a small knowledge base.

This is a starting point for further development. The knowledge base and NLP logic can be expanded to support more complex queries, RAG integration, and personalization features.
