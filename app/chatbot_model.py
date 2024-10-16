import pickle
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from config import Config
from fuzzywuzzy import process  # Ensure you have fuzzywuzzy installed

# Load configuration
MODEL_PATH = Config.MODEL_PATH
VECTORIZER_PATH = Config.VECTORIZER_PATH
FAQ_DATA_PATH = Config.FAQ_DATA_PATH

# Load trained model and vectorizer with error handling
try:
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
except FileNotFoundError:
    print(f"Error: Model file not found at {MODEL_PATH}.")
    exit(1)

try:
    with open(VECTORIZER_PATH, 'rb') as f:
        vectorizer = pickle.load(f)
except FileNotFoundError:
    print(f"Error: Vectorizer file not found at {VECTORIZER_PATH}.")
    exit(1)

# Load FAQ data with error handling
try:
    with open(FAQ_DATA_PATH, 'r') as f:
        faq_data = json.load(f)
except FileNotFoundError:
    print(f"Error: FAQ data file not found at {FAQ_DATA_PATH}.")
    exit(1)

def get_response(user_input):
    user_input_vector = vectorizer.transform([user_input])
    intent = model.predict(user_input_vector)[0]
    
    # Retrieve relevant FAQs based on intent
    if intent in faq_data:
        # Find the best matching question using fuzzy matching
        faq_questions = [faq["question"] for faq in faq_data[intent]]
        best_match, _ = process.extractOne(user_input, faq_questions)

        # Return the answer for the best matching question
        if best_match:
            for faq in faq_data[intent]:
                if faq["question"] == best_match:
                    return faq["answer"]
        return "I couldn't find an exact answer, but you can check our Help section or contact support."
    else:
        return "Sorry, I couldn't find an answer. Please check our Help section or contact support."
