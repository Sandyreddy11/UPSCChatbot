import unittest
from chatbot import get_answer, load_data

class ChatbotTests(unittest.TestCase):
    def setUp(self):
        self.data = load_data()

    def test_known_question(self):
        ans = get_answer('What is UPSC?', self.data)
        self.assertIn('Union Public Service Commission', ans)

    def test_unknown_question(self):
        ans = get_answer('What is the color of the sky?', self.data)
        self.assertEqual('Sorry, I don\'t have an answer for that.', ans)

if __name__ == '__main__':
    unittest.main()
