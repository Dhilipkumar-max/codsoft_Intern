def chatbot():
    print("Hello! I am RuleBot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ['hello', 'hi', 'hey']:
            print("RuleBot: Hello! How can I help you today?")
        
        elif "how are you" in user_input:
            print("RuleBot: I'm just a bunch of code, but I'm doing great! Thanks for asking.")

        elif "your name" in user_input:
            print("RuleBot: I am RuleBot, your friendly assistant.")

        elif "help" in user_input:
            print("RuleBot: I can help you with general questions. Try asking me about the weather, time, or anything!")

        elif "time" in user_input:
            from datetime import datetime
            print("RuleBot: Current time is", datetime.now().strftime("%H:%M:%S"))

        elif "weather" in user_input:
            print("RuleBot: I can't check real-time weather yet, but it looks like a good day!")

        elif user_input in ['bye', 'exit', 'quit']:
            print("RuleBot: Goodbye! Have a nice day!")
            break

        else:
            print("RuleBot: Sorry, I didn't understand that. Can you try again?")


# Run the chatbot
chatbot()