from django.contrib import admin
from .models import MiniApp

@admin.register(MiniApp)
class MiniAppAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'description')
    list_filter = ('id', 'name')
    search_fields = ('name', 'slug', 'description')
    prepopulated_fields = {'slug': ('name',)}