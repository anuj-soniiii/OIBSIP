import requests
# We install pip request 

api_key = "376059a2b40999b97ed8db3b6db20fd3"
# our api key 

city = input("Enter your city name: ")
# take a input from user for a city

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
# It is our url for searching weather 

response = requests.get(url)

if response.status_code == 200:


    data = response.json()

    temperature = data["main"]["temp"]

    humidity = data["main"]["humidity"]

    description = data["weather"][0]["description"]

# now we print all the factor about our weather like temprature, discription.

    print(f"\nWeather in {city.capitalize()}:")

    print(f"Temperature: {temperature}°C")
    
    print(f"Humidity: {humidity}%")

    print(f"Condition: {description.capitalize()}")

else:

    print("City not found or error fetching data.")
