import nltk
nltk.download('vader_lexicon')



import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')  # Download the sentiment lexicon

# Function to analyze sentiment
def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)
    
    if sentiment['compound'] >= 0.05:
        return "positive"
    elif sentiment['compound'] <= -0.05:
        return "negative"
    else:
        return "neutral"

def chatbot():
    print("Hello! I'm your chatbot. Type 'bye' or 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()  # Get user input and convert it to lowercase
        
        if user_input in ['bye', 'exit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        # Sentiment Analysis
        sentiment = analyze_sentiment(user_input)
        if sentiment == 'positive':
            print("Chatbot: I'm glad you're feeling good! 😊")
        elif sentiment == 'negative':
            print("Chatbot: Oh no! I hope things get better. 😞")
        else:
            print("Chatbot: Thanks for sharing! How can I assist you further?")
        
# Run the chatbot
chatbot()
