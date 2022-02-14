import requests #pip install requests; if having trouble make sure your pip folder is in path of environmental variables

# API key taken from personal openweather account
API_KEY = "cdf16ec5f400081e09fd32ecc6b931dc"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather" #base url can be found on their website through "open doc"

# user input
city = input("What city would you like to check the forecast of?: ")

request_url = "{}?appid={}&q={}".format(BASE_URL, API_KEY, city) #use of format string

# Get request to retrieve data
response = requests.get(request_url)

if response.status_code == 200: #200 is typical status code for "OK"
    data = response.json()
    weather = data['weather'][0]['description']
    print("The current forecast is: ", weather)
    temperature = data['main']["temp"]
    temperature_in_F = round(1.8 *(temperature - 273.15) + 32, 2)
    temperature_in_C = round(temperature - 273.15, 2)
    print("The current temperature in fahrenheit is: ", temperature_in_F,"F")
    print("The current temperature in celsius is: ", temperature_in_C,"C")
else:
    print("An error has occured. Apologies for the inconvenience :(")
