from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls')),
    path('', include('miniapp.urls'))
]