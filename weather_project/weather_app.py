import requests
import csv
from datetime import datetime

API_KEY = "88fd20ca33957b1168683a71b33a6d24"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    if int(data.get("cod", 0)) != 200:
        print("API ERROR:", data)
        return


    weather_info = {
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "description": data["weather"][0]["description"],
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    save_to_csv(weather_info)
    display_weather(weather_info)

def save_to_csv(data):
    with open("weather_data.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            data["city"],
            data["temperature"],
            data["humidity"],
            data["description"],
            data["date"]
        ])

def display_weather(data):
    print("\nWeather Report")
    print("----------------")
    print(f"City: {data['city']}")
    print(f"Temperature: {data['temperature']} °C")
    print(f"Humidity: {data['humidity']} %")
    print(f"Condition: {data['description']}")

if __name__ == "__main__":
    city_name = input("Enter city name: ")
    get_weather(city_name)
