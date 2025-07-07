from dotenv import load_dotenv
import os
import requests

load_dotenv()

api_key = os.getenv("API_KEY")
base_url = "https://api.weatherapi.com/v1"
current_weather_endpoint = "/current.json"
location = "28.71183637112679, 77.07249315556749"

url = f"{base_url}{current_weather_endpoint}?key={api_key}&q={location}"
weather_data = requests.get(url)
print(weather_data.status_code)
print(weather_data.text)
