import requests

def get_weather_by_city(city_name):
    url = 'https://goweather.herokuapp.com/weather/Moscow'
    weather = requests.get(url).json()
    return weather
# print(get_weather_by_city('Kazan'))
print(get_weather_by_city('Praha'))
# print(weather)
# print(type(weather))
# print(weather.keys())
# print(weather['temperature'])

