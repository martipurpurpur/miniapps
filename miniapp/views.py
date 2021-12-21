from django.shortcuts import render
from .models import miniapp_db


def miniapp(request, pk):
    name = miniapp_db[pk]['name']
    description = miniapp_db[pk]['description']
    context = {
        'name': name,
        'description': description,
    }
    return render(request, 'homepage/app.html', context)