class SimpleChatbot:
    def __init__(self):
        self.responses = {
            "hi": "Hello! How can I assist you?",
            "hello": "Hi there! How can I help you today?",
            "how are you": "I'm just a chatbot, but thanks for asking!",
            "what is your name": ["I'm just a humble chatbot!", "I'm ChatBot, nice to meet you!"],
            "who created you": ["I was created by OpenAI.", "My creator is a team of talented developers at OpenAI."],
            "bye": "Goodbye! Have a great day!",
            "thank you": "You're welcome! If you need anything else, feel free to ask."
        }

    def respond(self, message):
        message = message.lower()
        if message in self.responses:
            return self.responses[message]
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase?"

    def start_chat(self):
        print("Welcome to SimpleChatbot!")
        print("You can start chatting. Type 'bye' to end the conversation.")
        while True:
            user_input = input("You: ")
            if user_input.lower() == 'bye':
                print(self.respond(user_input))
                break
            print("Bot:", self.respond(user_input))


# Example usage:
chatbot = SimpleChatbot()
chatbot.start_chat()
