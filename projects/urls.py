from django.urls import path
from .views import PROJECT

urlpatterns = [
    path('project/', PROJECT ,name='project'),

]