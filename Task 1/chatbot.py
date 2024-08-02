import time
import random

now = time.ctime()

responses = {
    "greetings": ["Hi there! I'm a chatbot here to assist you.", "Hello! How can I help you today?"],
    "name": ["I'm just a chatbot, so I don't have a name, but you can call me anything."],
    "origin": ["I'm from the digital world, always ready to chat!"],
    "how_are_you": ["I'm fine."],
    "joke": ["Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "time": [now],
    "product": ["Our product is top-notch and has excellent reviews!", "You can find all product details on our website."],
    "technical_support": ["Please visit our technical support page for detailed assistance.", "You can also call our tech support helpline for immediate help."],
    "return_policy": ["We have a 30-day return policy.", "Please ensure the product is in its original condition when returning."],
    "help": ["How can I assist you further?", "Is there anything else you'd like to know?"],
    "default": ["I'm sorry, I didn't quite understand that. Can you please rephrase?", "My apologies, can you provide more details?"]
}

def chatbot(user_input, user_name):
    user_input = user_input.lower()
    
    if "hi" in user_input or "hello" in user_input:
        return f"{random.choice(responses['greetings'])} How can I assist you today, {user_name}?"
    elif "what is your name" in user_input:
        return random.choice(responses["name"])
    elif "where are you from" in user_input:
        return random.choice(responses["origin"])
    elif "how are you" in user_input:
        return random.choice(responses["how_are_you"])
    elif "tell me a joke" in user_input or "another joke" in user_input:
        return random.choice(responses["joke"])
    elif "what is the time now" in user_input:
        return random.choice(responses["time"])
    elif "bye" in user_input:
        return "Goodbye! Take care and have a great day!"
    elif "product" in user_input:
        return random.choice(responses["product"])
    elif "technical support" in user_input:
        return random.choice(responses["technical_support"])
    elif "return policy" in user_input:
        return random.choice(responses["return_policy"])
    elif "help" in user_input:
        return random.choice(responses["help"])
    else:
        return random.choice(responses["default"])

print("Chatbot: Hi! I'm a simple chatbot, I'm here to assist you!")

user_name = input("Chatbot: May I know your name?\nMe: ")

while True:
    user_input = input("Me: ")
    if user_input.lower() == 'bye':
        print(f"Chatbot: Goodbye, {user_name}! Have a great day!")
        break
    
    response = chatbot(user_input, user_name)
    print(f"Chatbot: {response}")
