def chatbot():
    print("Chatbot Started! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user in ["hello", "hi", "hii", "hey"]:
            print("Bot: Hi!")
        elif user == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user == "what is your name":
            print("Bot: I am a simple Python chatbot.")    
        elif user == "bye":
            print("Bot: Goodbye!")
            break
        else:
            print("Bot: Sorry, I don't understand.")

chatbot()
