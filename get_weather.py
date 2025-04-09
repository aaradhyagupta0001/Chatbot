import requests

def get_weather(city):
    # OpenWeatherMap API URL
    api_key = "your_api_key_here"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Complete URL
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    
    # Send request to API and get the response
    response = requests.get(complete_url)
    
    # Convert the response to JSON format
    data = response.json()
    
    # Check if the city is found
    if data["cod"] == 200:
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temp = main["temp"]
        print(f"The weather in {city} is {weather_desc} with a temperature of {temp}°C.")
    else:
        print("City not found, please try again.")

# Modify the chatbot function to respond to weather queries
def chatbot():
    print("Hello! I'm your chatbot. Type 'bye' or 'exit' to end the conversation.")
    
    while True:
        user_input = input("You: ").lower()  # Get user input and convert it to lowercase
        
        if user_input in ['bye', 'exit']:
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        elif 'weather' in user_input:  # Check if user asks about weather
            city = input("Which city do you want the weather for? ")
            get_weather(city)
        
        elif user_input in ['hello', 'hi']:
            print("Chatbot: Hello! How can I help you today?")
        
        elif user_input in ['how are you']:
            print("Chatbot: I'm doing great! How about you?")
        
        else:
            print("Chatbot: Sorry, I didn't understand that. Can you ask something else?")
            
# Run the chatbot
chatbot()
