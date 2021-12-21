from django.http import HttpResponse
from django.shortcuts import render
import datetime
import requests

def index(request):
    current_date = datetime.date.today().strftime('%d.%m.%Y')
    url = 'https://wttr.in'

    weather_parameters = {
        'format': 2,
        'M': ''
    }
    response = requests.get(url, params=weather_parameters)
    context = {
    'title': 'Мини-приложения',
    'date': current_date,
    'weather': response.text,
    'main_text': ('На все случаи жизни')
    }
    return render(request, 'homepage/index.html', context)

def about(request):
    return HttpResponse('что-то обо мне -- ¯\(°:°)/¯')