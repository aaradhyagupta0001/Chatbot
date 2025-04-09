# Simple Chatbot in Python

# Function to handle chatbot responses
def chatbot():
    print("Hello! I'm your chatbot. Type 'bye' or 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()  # Get user input and convert it to lowercase for simplicity
        
        # Check if user wants to exit
        if user_input in ['bye', 'exit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Chatbot responses
        elif user_input in ['hello', 'hi']:
            print("Chatbot: Hello! How can I help you today?")
        
        elif user_input in ['how are you', 'how are you doing']:
            print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
        
        elif user_input in ['what is your name', 'who are you']:
            print("Chatbot: I'm just a simple chatbot created by you!")
        
        elif user_input in ['tell me a joke']:
            print("Chatbot: Why don't skeletons fight each other? Because they don't have the guts!")
        
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you ask something else?")
            
# Call the chatbot function to start the conversation
chatbot()
