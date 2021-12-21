from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls')),
    path('miniapp/', include('miniapp.urls'))
]