# app.py

from flask import Flask, request, render_template,jsonify
import os

openai_api_key = os.environ.get('OPENAI_API_KEY')
import openai

openai.api_key = openai_api_key


app = Flask(__name__)

# Simple chatbot response function
def get_bot_response(message):
 
    
    # Financial Support for Farmers
    if any(word in message.lower() for word in ['financial support', 'agricultural loans', 'grants', 'support programs']):
        return "Absolutely. Our financial resources section has information on agricultural loans, grants, and support programs. Is there a specific type of financial assistance you need?"
    
    # Forum Registration
    elif any(word in message.lower() for word in ['join the forum', 'forum registration']):
        return "To join the forum, follow the registration steps. Feel free to ask if you need any assistance during the process."
    
    # Contribution to the Platform
    elif any(word in message.lower() for word in ['contribute', 'join us', 'share knowledge']):
        return "We welcome contributions! You can share your knowledge by submitting articles or resources. Visit the 'Join Us' section for more details and guidelines."
    
    # Pest and Disease Management
    elif any(word in message.lower() for word in ['pest', 'disease', 'crop protection']):
        return "For pest and disease management tips, check out our resources on crop protection and pest control. Feel free to ask specific questions if you need further assistance."
    
    # Crop Cultivation Techniques
    elif any(word in message.lower() for word in ['crop cultivation', 'farming techniques', 'best practices']):
        return "Explore our guides on crop cultivation techniques and best farming practices to optimize your yields and improve productivity."
    
    # Market Access and Marketing Strategies
    elif any(word in message.lower() for word in ['market access', 'marketing strategies', 'sell crops']):
        return "Learn about market access strategies and effective marketing techniques to sell your crops profitably. Our resources cover topics such as value chain analysis and market intelligence."
    
    # Weather and Climate Information
    elif any(word in message.lower() for word in ['weather forecast', 'climate information', 'seasonal farming']):
        return "Stay informed about weather forecasts and seasonal farming practices to adapt your farming activities accordingly. Our platform provides access to reliable climate information and farming calendars."
    
    # General Assistance
  # Use ChatGPT for other queries
    else:
        # Generate a response using ChatGPT
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=message,
            max_tokens=50
        )
        return response.choices[0].text.strip()


    

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
