import os
import winreg as reg
import requests
import pyttsx3
from datetime import datetime
import speech_recognition as sr
import ollama  # Import the Ollama client

# Initialize the Ollama client
client = ollama.Client()

# Function to add the script to Windows startup
def add_to_startup(file_path=None):
    if file_path is None:
        file_path = os.path.abspath(__file__)
    key = reg.HKEY_CURRENT_USER
    key_value = r"Software\Microsoft\Windows\CurrentVersion\Run"
    with reg.OpenKey(key, key_value, 0, reg.KEY_ALL_ACCESS) as reg_key:
        reg.SetValueEx(reg_key, "JARVIS", 0, reg.REG_SZ, file_path)

# Function to fetch current time
def get_current_time():
    return datetime.now().strftime("%H:%M:%S")

# Function to generate a greeting based on the time of day
def get_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning Boss!"
    elif 12 <= hour < 15:
        return "Good afternoon Boss!"
    elif 15 <= hour < 19:
        return "Good evening Boss!"
    else:
        return "Good night Boss!"

# Function to fetch weather data
def get_weather(api_key, location):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            return f"The weather in {location} is {data['main']['temp']}°C with {data['weather'][0]['description']}."
        else:
            return "Unable to fetch weather data."
    except Exception as e:
        return "Error fetching weather data."

# Function to fetch news headlines
def get_news(api_key, country='us'):
    try:
        url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            articles = data['articles'][:3]
            return "Here are the top news headlines: " + " ".join([article['title'] for article in articles])
        else:
            return "Unable to fetch news."
    except Exception as e:
        return "Error fetching news."

# Function to convert text to speech
def speak(text):
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print("Error in text-to-speech:", e)

# Function to interact with LLaMA 2
def chat_with_llama(prompt):
    # Send the query to the model
    response = client.generate(model="llama2", prompt=prompt)
    return response.response  # Return the response from the model

# Function to recognize speech and convert it to text
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            return recognizer.recognize_google(audio)
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except Exception as e:
            return "Error recognizing speech."

# Main function
def main():
    # Configuration
    weather_api_key = "14027c98399d7448dd775e0441f7e37e"  # Replace with your OpenWeatherMap API key
    news_api_key = "c908be664ca44cd3a0fc493621c69b91"  # Replace with your NewsAPI key
    location = "Bhubaneshwar"  # Replace with your city name

    # Get greeting based on the time of day
    greeting = get_greeting()

    # Fetch current time
    current_time = get_current_time()
    print(f"Current time: {current_time}")

    # Fetch weather
    weather = get_weather(weather_api_key, location)
    print(f"Weather: {weather}")

    # Fetch news
    news = get_news(news_api_key)
    print(f"News: {news}")

    # Combine the message to speak
    message = f"{greeting} The current time is {current_time}. {weather} {news}"

    # Speak the combined message
    print("Speaking message...")
    speak(message)

    # Transition to LLaMA 2 voice assistant
    print("Switching to LLaMA 2 assistant...")
    speak("I am ready to assist you. Please ask me anything.")

    while True:
        user_input = recognize_speech()
        if user_input.lower() in ["exit", "bye"]:
            speak("Goodbye Boss! Have a great day!")
            break

        if user_input:
            response = chat_with_llama(user_input)
            print(f"LLaMA 2: {response}")
            speak(response)

if __name__ == "__main__":
    # Add the script to startup (optional, run once to register)
    add_to_startup()

    # Run the main logic
    main()