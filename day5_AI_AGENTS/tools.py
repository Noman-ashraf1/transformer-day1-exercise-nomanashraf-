
import requests
import math


def calculator(expression: str):
    """Evaluate a mathematical expression."""
    try:
        return eval(expression)
    except Exception:
        return "Invalid expression"





def web_search(query: str):
    """
    Simple search tool.
    Uses DuckDuckGo instant answer API.
    """
    try:
        url = f"https://api.duckduckgo.com/?q={query}&format=json"
        data = requests.get(url).json()

        if data["AbstractText"]:
            return data["AbstractText"]

        return "No search result found."

    except Exception:
        return "Search failed."


def weather(city: str):
    """
    Weather tool using Open-Meteo API.
    """
    try:

        geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
        geo = requests.get(geo_url).json()

        lat = geo["results"][0]["latitude"]
        lon = geo["results"][0]["longitude"]

        weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
        weather_data = requests.get(weather_url).json()

        temp = weather_data["current_weather"]["temperature"]

        return f"Current temperature in {city} is {temp}°C"

    except Exception:
        return "Weather data unavailable."