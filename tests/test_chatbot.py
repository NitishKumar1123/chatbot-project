# test_chatbot.py
import sys
import os

# Add the project root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from app.chatbot_model import get_response

class TestChatbot(unittest.TestCase):

    def test_payment_intent(self):
        user_input = "How can I make a payment?"
        response = get_response(user_input)
        self.assertIn("You can pay via", response)

    def test_return_policy_intent(self):
        user_input = "What is your return policy?"
        response = get_response(user_input)
        self.assertIn("You can return products", response)

    def test_unknown_intent(self):
        user_input = "Tell me a joke."
        response = get_response(user_input)
        self.assertEqual(response, "Sorry, I couldn't find an answer. Please check our Help section or contact support.")

if __name__ == '__main__':
    unittest.main()
