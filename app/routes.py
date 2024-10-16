from flask import Blueprint, render_template, request, jsonify
from .chatbot_model import get_response

chatbot_bp = Blueprint('chatbot', __name__)

@chatbot_bp.route('/')
def index():
    return render_template('index.html')

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get('message')
    if not user_message:
        return jsonify({'response': "Please enter a message."})
    
    bot_response = get_response(user_message)
    return jsonify({'response': bot_response})
