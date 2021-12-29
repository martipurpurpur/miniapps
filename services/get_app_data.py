
from miniapps.models import MiniApp
from random import randint
import requests

def get_app_data(params, slug):
    if slug == 'randomizer':
        result = randomizer(params)
    elif slug == 'weather':
        result = weather(params)
    elif slug == 'telegrambot':
        result = telegrambot(params)
    else:
        result = None
    return result

def worldtime(params):
    city = params['city']
    result = city
    return result

def randomizer(params):
    min = int(params['min_rand'][0])
    max = int(params['min_rand'][0])
    result = randint(min, max)
    return result

def telegrambot(params):
    result = params
    return result

def weather(params):
    city = params['city'][0]
    url = f'https://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    response = requests.get(url, params=weather_parameters)
    return response.text