import requests

API_KEY = "4e69835fd7c0ee0346ea937b3a05e8c2"  # replace this with your real OpenWeatherMap API key

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    
    try:
        response = requests.get(url)
        data = response.json()

        if data.get("cod") == 200:
            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind = data["wind"]["speed"]

            return (
                f"Weather in {city}:\n"
                f"Temperature: {temp}°C\n"
                f"Description: {desc}\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind} m/s"
            )
        else:
            return "City not found."

    except Exception as e:
        return f"Error: {e}"

# ---- Start the app ----
city = input("Enter a city: ")
print(get_weather(city))
