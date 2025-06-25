import json

from chatbot.app import app


def test_ping():
    with app.test_client() as client:
        resp = client.get('/ping')
        assert resp.status_code == 200
        assert resp.get_json() == {"status": "ok"}


def test_chat_known_question():
    with app.test_client() as client:
        resp = client.post('/chat', json={"message": "What is UPSC Prelims"})
        data = resp.get_json()
        assert resp.status_code == 200
        assert "two objective papers" in data["answer"].lower()


def test_chat_unknown_question():
    with app.test_client() as client:
        resp = client.post('/chat', json={"message": "Who won the world cup?"})
        data = resp.get_json()
        assert resp.status_code == 200
        assert "don't have an answer" in data["answer"].lower()
