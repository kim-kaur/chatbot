# chatbot.py

def chatbot():
    print("Hello! I’m ChatBot 🤖. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Bot: Hello! How can I help you today?")
        
        elif "your name" in user_input:
            print("Bot: I’m a simple chatbot built with Python if-else.")
        
        elif "how are you" in user_input:
            print("Bot: I’m doing great, thank you! How about you?")
        
        elif "help" in user_input:
            print("Bot: Sure! I can answer simple questions like greetings, my name, or how I am.")
        
        elif user_input == "bye":
            print("Bot: Goodbye! Have a nice day 😊")
            break
        
        else:
            print("Bot: Sorry, I don’t understand that. Please try again.")

if __name__ == "__main__":
    chatbot()