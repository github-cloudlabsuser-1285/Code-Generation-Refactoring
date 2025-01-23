import requests

def get_weather(city):
    api_key = "604adf9e1baa49587e34444c645a7355"  # Replace with your actual API key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key

    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]
        print(f"City: {city}")
        print(f"Temperature: {main['temp']}K")
        print(f"Weather: {weather['description']}")
    else:
        print("City not found")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)