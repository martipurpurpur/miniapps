from django.shortcuts import render
from .models import miniapp_db
from services import *


def miniapp(request, pk):
    name = miniapp_db[pk]['name']
    description = miniapp_db[pk]['description']
    context = {
        'name': name,
        'description': description,
    }
    if name == "Рандомайзер":
        return render(request, 'homepage/apps/app_random.html', context)
    elif name == "Мировое время":
        return render(request, 'homepage/apps/app_time.html', context)
    else:
        return render(request, 'homepage/404.html')


def about(request):
    return render(request, 'homepage/about.html')