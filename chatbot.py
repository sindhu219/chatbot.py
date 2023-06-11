import random

# Define chatbot responses
responses = {
    "hello": ["Hello!", "Hi there!", "Greetings!"],
    "how_are_you": ["I'm doing well, thank you!", "I'm great! How about you?", "All good!"],
    "goodbye": ["Goodbye!", "See you later!", "Farewell!"],
    "thanks": ["You're welcome!", "No problem!", "Glad I could help!"],
    "name": ["I am a chatbot.", "You can call me ChatBot.", "I don't have a name, but I'm here to assist you!"],
    "age": ["I'm a chatbot, so I don't have an age!", "I exist in the digital realm, ageless and timeless!"],
    "default": ["I'm sorry, I didn't understand.", "Can you please rephrase that?", "I'm still learning!"]
}

# Function to generate chatbot responses
def get_response(message):
    message = message.lower()

    if message.startswith("hello"):
        return random.choice(responses["hello"])
    elif "how are you" in message:
        return random.choice(responses["how_are_you"])
    elif message.startswith("goodbye"):
        return random.choice(responses["goodbye"])
    elif "thank" in message:
        return random.choice(responses["thanks"])
    elif "name" in message:
        return random.choice(responses["name"])
    elif "age" in message:
        return random.choice(responses["age"])
    else:
        return random.choice(responses["default"])

# Main loop for user interaction
print("Chatbot: Hello! How can I assist you today?")
while True:
    user_input = input("User: ")
    response = get_response(user_input)
    print("Chatbot:", response)
