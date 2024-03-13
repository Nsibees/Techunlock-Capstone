# app.py

from flask import Flask, request, render_template,jsonify

app = Flask(__name__)

# Simple chatbot response function
def get_bot_response(message):
    # Implement logic to handle emergency-related queries
    # For simplicity, let's provide generic responses
    if 'Can you recommend financial support for farmers' in message.lower():
        return "Absolutely. Our financial resources section has information on agricultural loans, grants, and support programs. Is there a specific type of financial assistance you need?"
    elif 'How can I join the forum' in message.lower():
        return "To join the forum, follow the registration steps. Feel free to ask if you need any Assitance during the process."
    elif 'How can I contribute to the platform?' in message.lower():
        return "We welcome contributions! You can share your knowledge by submitting articles or resources. Visit the 'Join Us' section for more details and guidelines."
    else:
        return "I'm sorry, I didn't understand that. For more support and information, please dial 111."

# Chatbot route
@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json['message']
    bot_response = get_bot_response(user_message)
    return jsonify({'response': bot_response})

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
