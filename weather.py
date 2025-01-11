import requests
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENWEATHER_API_KEY')

def get_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        return f'The weather in {city} is {weather} with a temperature of {temperature}°C.'
    else:
        return f"Sorry, I could not retrieve the weather information for {city}."
