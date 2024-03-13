// scripts.js
const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');

function sendMessage() {
    const message = userInput.value.trim();
    if (message === '') return;

    appendMessage('You', message);
    userInput.value = '';

    fetch('/chatbot', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message })
    })
        .then(response => response.json())
        .then(data => appendMessage('Bot', data.response))
        .catch(error => console.error('Error:', error));
}

function appendMessage(sender, message) {
    const messageElement = document.createElement('div');
    messageElement.textContent = `${sender}: ${message}`;
    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
}


// Function to toggle the visibility of the chat pop-up
function toggleChat() {
    var chatPopup = document.getElementById("chatPopup");
    chatPopup.classList.toggle("show");
}
//e5e0bea5a0879b07cfdf2fe5bb19ebd4
// Function to fetch weather data from OpenWeatherMap API
function getWeather(Nigeria) {
    const apiKey = 'e5e0bea5a0879b07cfdf2fe5bb19ebd4';
    const apiUrl = `https://home.openweathermap.org/api_keys`;

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            const temperature = data.main.temp;
            const description = data.weather[0].description;
            const message = `The weather in ${city} is ${description} with a temperature of ${temperature}°C.`;
            displayMessage(message);
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
            displayMessage('Sorry, I couldn\'t retrieve the weather information at the moment. Please try again later.');
        });
}

// Function to display message in chatbot interface
function displayMessage(message) {
    // Display message in chat window
}

// Example usage: User asks for weather
const userQuery = 'What\'s the weather like in Ikorodu today?';
const country = 'Nigeria';
if (userQuery.toLowerCase().includes('weather')) {
    getWeather(country);
}