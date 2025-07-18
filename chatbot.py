import json
import difflib

DATA_FILE = 'qa_pairs.json'


def load_data(path=DATA_FILE):
    """Load question and answer pairs from a JSON file."""
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def get_answer(question, data):
    """Return the best matching answer for the given question."""
    questions = [item['question'] for item in data]
    lower_questions = [q.lower() for q in questions]
    matches = difflib.get_close_matches(question.lower(), lower_questions, n=1, cutoff=0.6)
    if matches:
        idx = lower_questions.index(matches[0])
        return data[idx]['answer']
    return "Sorry, I don't have an answer for that."


def main():
    data = load_data()
    print("Welcome to UPSC Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input('You: ').strip()
        if user_input.lower() in {'exit', 'quit'}:
            print('Chatbot: Goodbye!')
            break
        response = get_answer(user_input, data)
        print(f'Chatbot: {response}')


if __name__ == '__main__':
    main()
