from django.shortcuts import render
import django.template.exceptions as e
from services.get_app_data import get_app_data
from .models import MiniApp


def miniapp(request, slug):
    app = MiniApp.objects.get(slug=slug)
    name = app.name
    slug = app.slug
    description = app.description

    context = {
        'slug': slug,
        'name': name,
        'description': description,
    }
    try:
        return render(request, f'homepage/apps/{slug}.html', context)
    except e.TemplateDoesNotExist:
        return render(request, 'homepage/404.html')

def miniapp_post(request, slug):
    app = MiniApp.objects.get(slug=slug)
    name = app.name
    slug = app.slug
    description = app.description
    params = request.POST
    result = get_app_data(params, slug)
    context = {
        'slug': slug,
        'name': name,
        'description': description,
        'result': result
    }
    return render(request, f'homepage/apps/{slug}.html', context)

