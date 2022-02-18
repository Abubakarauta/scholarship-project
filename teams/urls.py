from django.urls import path
from .views import Team



urlpatterns=[
    path('team/', Team , name='team'),
]
    