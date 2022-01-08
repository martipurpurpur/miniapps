import codecs
import requests
from random import randint
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from pytz import timezone, utc
from datetime import datetime


def get_app_data(params, slug):
    if slug == 'randomizer':
        result = randomizer(params)
    elif slug == 'weather':
        result = weather(params)
    elif slug == 'telegrambot':
        result = telegrambot(params)
    elif slug == 'worldtime':
        result = worldtime(params)
    elif slug == 'encoder':
        result = encoder(params)
    else:
        result = None
    return result


def worldtime(params):
    city = params['city']
    geolocator = Nominatim(user_agent="multiapp")
    location = geolocator.geocode(city, language="en")
    points = {"lat": location.latitude, "lng": location.longitude}
    result = get_time(**points)
    return result


def randomizer(params):
    min = int(params['min_rand'])
    max = int(params['max_rand'])
    result = randint(min, max)
    return result


def telegrambot(params):
    result = params
    return result


def encoder(params):
    text = params['rot']
    result = codecs.encode(text, 'rot13')
    return result


def weather(params):
    city = params['city']
    url = f'https://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    response = requests.get(url, params=weather_parameters)
    return response.text


def get_time(*, lat, lng):
    """
    Getting formatted time by longitude and latitude
    """
    tf = TimezoneFinder()
    target_time_zone = timezone(tf.timezone_at(lat=lat, lng=lng))
    result_time = datetime.now(tz=target_time_zone)
    return result_time.strftime('%H:%M:%S %Z%z')