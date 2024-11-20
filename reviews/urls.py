from django.urls import path
from .views import all_reviews, add_review

urlpatterns = [
    path('', all_reviews, name='all_reviews'),
    path('add/', add_review, name='add_review'),
]
