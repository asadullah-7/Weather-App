import json

import requests
while True:


    city = input("Enter City: ")
    if city == 'q':
        break
    url = f"https://api.weatherapi.com/v1/current.json?key=36e1c7c4d4b44b1daab14641250909&q={city}"

    r =requests.get(url)

    wdic = json.loads(r.text)
    print("Temperature: ",wdic["current"]["temp_c"],"Celsius")
    print("Feels Like: ",wdic["current"]["feelslike_c"], "Celsius")
    print("Humidity: ",wdic["current"]["humidity"],"%")
    print("cloud: ",wdic["current"]["cloud"],"%")
    print("condition: ",wdic["current"]["condition"]["text"])