from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.miniapp),
    path('about/', views.about)
]