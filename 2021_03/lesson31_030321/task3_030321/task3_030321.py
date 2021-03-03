# task3_030321
"""
The Weather app
Write a console application which takes as an input a city name and returns current weather in the format of your choice.
For the current task, you can choose any weather API or website or use https://openweathermap.org
"""

import requests


def set_url(city_name, key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}'
    return url


def get_weather_data(url):
    response = requests.get(url)
    return response.json()


def print_weather(data, city_name):
    print("{}'s temperature: {}°C ".format(city_name, data['main']['temp']))
    print("Wind speed: {} m/s".format(data['wind']['speed']))
    print("Description: {}".format(data['weather'][0]['description']))
    print("Weather: {}".format(data['weather'][0]['main']))


if __name__ == '__main__':
    api_key = 'd71fe15a0a40cbd435427e14549a55ca'
    city = input('Enter the city:')
    print()
    print(set_url(city, api_key))

    weather_data = get_weather_data(set_url(city, api_key))
  #  print_weather(weather_data, city)
    print(weather_data)
