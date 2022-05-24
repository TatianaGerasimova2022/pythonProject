import requests

def get_weather_by_city(city_name):
    url = 'https://goweather.herokuapp.com/weather/Moscow'
    weather = requests.get(url).json()
    return weather
# print(get_weather_by_city('Kazan'))
print(get_weather_by_city('Praha'))
print(get_weather_by_city('Praha123'))
print(get_weather_by_city('Praha123456'))
print(get_weather_by_city('Praha1234568910'))
# print(weather)
# print(type(weather))
# print(weather.keys())
# print(weather['temperature'])

