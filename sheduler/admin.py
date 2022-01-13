from django.contrib import admin
from .models import Sheduler

@admin.register(Sheduler)
class ShedulerAdmin(admin.ModelAdmin):
    list_display = ('id', 'day', 'shedule', 'time')
    list_filter = ('id', 'day', 'shedule')
    search_fields = ('id', 'day', 'shedule', 'time')
