from django.urls import path
from .views import booking_form

urlpatterns = [
    path('', booking_form, name='booking_form'),
]
