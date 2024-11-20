from django.urls import path
from .views import wedding_services, evening_services, nude_services, thematic_services

urlpatterns = [
    path('wedding/', wedding_services, name='wedding_services'),
    path('evening/', evening_services, name='evening_services'),
    path('nude/', nude_services, name='nude_services'),
    path('thematic/', thematic_services, name='thematic_services'),
]
