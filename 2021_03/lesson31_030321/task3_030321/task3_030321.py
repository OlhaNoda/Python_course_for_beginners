# task3_030321
"""
The Weather app
Write a console application which takes as an input a city name and returns current weather in the format of your choice.
For the current task, you can choose any weather API or website or use https://openweathermap.org
"""

import requests
import datetime


def set_url(city_name, key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={key}'
    return url


def get_weather_data(url):
    ret = requests.get(url)
    return ret.json()


def transform_unix_time(unix_time):
    value = datetime.datetime.fromtimestamp(unix_time)
    return value.strftime('%Y-%m-%d %H:%M:%S')


def print_weather(data, city_name):
    print("{}'s temperature: {}°C ".format(city_name, round(data['main']['temp']-273.15)))
    print("Wind speed: {} m/s".format(data['wind']['speed']))
    print("Weather: {}".format(data['weather'][0]['description']))
    print("Sunrise: {}".format(transform_unix_time(data['sys']['sunrise'])))
    print("Sunset: {}".format(transform_unix_time(data['sys']['sunset'])))


if __name__ == '__main__':
    api_key = '14ecba0ff417be47073468f7e5b4c133'
    city = input('Enter the city:')
    print_weather(get_weather_data(set_url(city, api_key)), city)
