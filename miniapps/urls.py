from django.urls import path
from miniapps import views

app_name = 'miniapps'

urlpatterns = [
    path('<slug:slug>/', views.miniapp),
    path('<slug:slug>/update/', views.miniapp_post),
]