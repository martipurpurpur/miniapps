from django.urls import path
from . import views

urlpatterns = [
    path('', views.miniapp_list),
    path('<int:pk>/', views.miniapp)
]