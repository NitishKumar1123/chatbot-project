# Company FAQ Chatbot
# Overview
The Company FAQ Chatbot is an intelligent virtual assistant designed to enhance user experience by automating the process of answering frequently asked questions (FAQs) related to buying and paying processes. This chatbot leverages machine learning and natural language processing to provide accurate and relevant responses to user inquiries.

![image](https://github.com/user-attachments/assets/2e493faf-ef77-433a-8907-2aec14c362c4)

# Features
Intent Recognition: The chatbot utilizes a trained Logistic Regression model to accurately identify user intents.
Natural Language Processing: Advanced NLP techniques enable the chatbot to process and understand user queries effectively.
Fuzzy Matching: Incorporates fuzzy matching to return relevant FAQs even if user queries are not exact matches.
Dynamic Interface: Built with Flask, the chatbot features a user-friendly web interface that allows real-time interaction.
Error Handling: The chatbot gracefully manages errors related to user input and model loading, providing fallback responses.
# Tech Stack
Backend: Python, Flask
Machine Learning: Scikit-learn, FuzzyWuzzy
Frontend: HTML, CSS, JavaScript
Data Storage: JSON files for FAQs and training data
# Project Structure

company_chatbot/
├── app/
│   ├── __init__.py
│   ├── main.py                  
│   ├── routes.py                
│   ├── chatbot_model.py         
│   └── templates/
│       ├── index.html           
│       ├── chat_interface.html  
│   └── static/
│       ├── css/
│       │   └── styles.css       
│       ├── js/
│           └── chatbot.js       
├── data/
│   ├── faq_data.json             
│   └── training_data.json       
├── model/
│   ├── intent_model.pkl         
│   └── vectorizer.pkl           
├── scripts/
│   └── train_model.py           
├── tests/
│   └── test_chatbot.py          
├── config.py                    
├── requirements.txt             
└── run.py                       
Installation
# Clone the repository:

git clone https://github.com/NitishKumar1123/chatbot-project.git
# Navigate to the project directory:

cd chatbot-project
Install the required dependencies:

pip install -r requirements.txt
Usage
Start the Flask application:

python run.py
Open your web browser and go to http://127.0.0.1:5000 to interact with the chatbot.
Training the Model
To train the chatbot's intent recognition model, you can use the provided train_model.py script. Make sure to have your training data ready in data/training_data.json. Run the script as follows:

python scripts/train_model.py
Testing
Unit tests are included in the tests/ directory. To run the tests, navigate to the project directory and execute:

python -m unittest discover tests
Contributions
Contributions are welcome! If you have suggestions or improvements, feel free to fork the repository and submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
