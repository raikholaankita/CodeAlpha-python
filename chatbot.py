def get_bot_reply(user_text):
    user_text = user_text.lower().strip()
    greetings = ["hello", "hi", "hii", "hey", "namaste"] 
    bye_words = ["bye", "exit", "quit", "tata"]
    if user_text in greetings:
        return "Bot: Hii"
    elif "how are you" in user_text:
        return "Bot: I'm fine"
    elif "your name" in user_text:
        return "Bot: My name is Chatbot"
    elif user_text in bye_words:
        return "exit" 
    else:
        return "Bot: Sorry, samajh nahi aaya. 'hello', 'how are you', 'your name' ya 'bye' ."
print("=== BASIC CHATBOT ===")
print("Type 'bye' to exit")
while True:
    user_input = input("You: ")
    reply = get_bot_reply(user_input)
    if reply == "exit":
        print("Bot: Goodbye! Have a nice day!")
        break
    else:
        print(reply)