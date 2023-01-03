import requests

api_key = '30d4741c779ba94c470ca1f63045390a'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&exclude=hourly,daily&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print(f"There is no city like {user_input}")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])


    print(f"The weather in {user_input} is: {hourly}")
    print(f"The temperature in {user_input} is: {daily}ºC")

