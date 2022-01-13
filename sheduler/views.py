from django.shortcuts import render
from .models import Sheduler


def get_all_days():
    all_days = Sheduler.objects.all()
    return all_days

def get_day(day):
    day = Sheduler.objects.get(day=day)
    return day

def time_over(day):
    time_over = Sheduler.objects.get(day=day)
    return time_over

# def get_all_days(request):
#     all_days = Sheduler.objects.all()
#     return render(request, all_days)
#
#
# def get_day(request, day):
#     day = Sheduler.objects.get(day=day)
#     return render(request, day)
#
#
# def time_over(request, day):
#     time_over = Sheduler.objects.get(day=day)
#     return render(request, time_over)