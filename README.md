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

Run the server and open [http://localhost:5000/](http://localhost:5000/) to try the
simple web interface located in `web/index.html`.

This minimal version does not require any external model API keys. Answers come
from the small in-memory knowledge base defined in `chatbot/knowledge_base.py`.
To expand coverage you can edit that file or train your own UPSC-focused model
using a suitable dataset and integrate it here.

This is a starting point for further development. The knowledge base and NLP logic can be expanded to support more complex queries, RAG integration, and personalization features.
