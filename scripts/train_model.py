import sys
import os

# Add the project root directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from config import Config  # This line should work now

def load_training_data(filepath):
    """Load training data from a JSON file."""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: The file {filepath} was not found.")
        sys.exit(1)
    except json.JSONDecodeError:
        print("Error: JSON decoding failed. Please check the file format.")
        sys.exit(1)

def train_and_save_model(training_data):
    """Train and save the model and vectorizer."""
    # Split the data
    X_train = [item['query'] for item in training_data]
    y_train = [item['intent'] for item in training_data]

    # Vectorize the text
    vectorizer = TfidfVectorizer()
    X_train_vectorized = vectorizer.fit_transform(X_train)

    # Train a simple classifier (Logistic Regression)
    model = LogisticRegression()
    model.fit(X_train_vectorized, y_train)

    # Ensure the model directory exists
    os.makedirs(os.path.dirname(Config.MODEL_PATH), exist_ok=True)

    # Save the model and vectorizer
    with open(Config.MODEL_PATH, 'wb') as model_file:
        pickle.dump(model, model_file)

    with open(Config.VECTORIZER_PATH, 'wb') as vectorizer_file:
        pickle.dump(vectorizer, vectorizer_file)

    print("Model and vectorizer trained and saved successfully.")

if __name__ == "__main__":
    # Load training data from a JSON file
    training_data_file = 'data/training_data.json'  # Ensure this file exists
    training_data = load_training_data(training_data_file)

    # Train the model and save it
    train_and_save_model(training_data)
