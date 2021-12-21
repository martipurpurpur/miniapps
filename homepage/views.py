#from django.http import HttpResponse
from django.shortcuts import render
import datetime
import requests
from miniapp.models import miniapp_db

def index(request):
    current_date = datetime.date.today().strftime('%d.%m.%Y')

    url = 'https://wttr.in'
    weather_parameters = {
        'format': 2,
        'M': ''
    }


    response = requests.get(url, params=weather_parameters)
    context = {
    'date': current_date,
    'weather': response.text,
    'miniapps': miniapp_db
    }
    return render(request, 'homepage/index.html', context)