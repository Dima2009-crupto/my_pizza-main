import os

import requests
from dotenv import load_dotenv


load_dotenv()


def get_wheather(city : str ="Kyiv"):
    api_key = os.getenv("WHEATHER_API")
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&g={city}"
    wheater = requests.get(url).json()
    
    data ={
        "city": city,
        "temp": wheater.get("current", {}).get("temp_c"),
        "text": wheater.get("current", {}).get("condition", {}).get("text"),
        "icon": wheater.get("current", {}).get("condition", {}).get("icon")
    }
    return data

