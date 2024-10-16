import os

class Config:
    # Paths for model and vectorizer
    MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'intent_model.pkl')
    VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), 'model', 'vectorizer.pkl')
    FAQ_DATA_PATH = os.path.join(os.path.dirname(__file__), 'data', 'faq_data.json')

    # Other configurations can be added as needed
