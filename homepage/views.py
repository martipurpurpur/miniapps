#from django.http import HttpResponse
from django.shortcuts import render
import datetime
import requests
from miniapps.models import MiniApp

def index(request):
    current_date = datetime.date.today().strftime('%d.%m.%Y')

    url = 'https://wttr.in'
    weather_parameters = {
        'format': 2,
        'M': ''
    }

    response = requests.get(url, params=weather_parameters)

    miniapps = MiniApp.objects.all()
    context = {
    'date': current_date,
    'weather': response.text,
    'miniapps': miniapps
    }
    return render(request, 'homepage/index.html', context)

def about(request):
    return render(request, 'homepage/about.html')