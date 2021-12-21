from django.shortcuts import render
from .models import miniapp_db


def miniapp_list(request):
    miniapps = ''
    for item in range(len(miniapp_db)):
        miniapps += f"<a href='{item}/'>{miniapp_db[item]['name']}</a><br>"
    context = {

        'title': 'Мини-приложения',
        'miniapps': miniapps
    }
    return render(request, 'miniapps/miniapps-list.html', context)


def miniapp(request, pk):
    name = miniapp_db[pk]['name']
    description = miniapp_db[pk]['description']
    context = {
        'name': name,
        'description': description,
    }
    return render(request, 'miniapps/app.html', context)