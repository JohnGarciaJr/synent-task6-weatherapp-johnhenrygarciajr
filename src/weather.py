import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch weather data for a given city."""
    if not API_KEY:
        return {
            "error": (
                "API key not found. Please set API_KEY "
                "in your .env file."
            )
        }

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "imperial"  # Fahrenheit
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200:
            return {"error": data.get("message", "Unknown error occurred.")}

        return data

    except requests.exceptions.RequestException:
        return {"error": "Network error. Please check your connection."}


def display_weather(data):
    """Format and print weather data."""
    if "error" in data:
        print(f"\n❌ Error: {data['error']}")
        return

    city = data["name"]
    country = data["sys"]["country"]
    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    condition = data["weather"][0]["description"].title()
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]

    print(f"\nWeather for {city}, {country}")
    print("-" * 30)
    print(f"Temperature: {temp}°F")
    print(f"Feels Like: {feels}°F")
    print(f"Condition: {condition}")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind} mph")


def main():
    print("=== Weather App ===")
    city = input("Enter a city name: ").strip()

    if not city:
        print("❌ Please enter a valid city name.")
        return

    data = get_weather(city)
    display_weather(data)


if __name__ == "__main__":
    main()
