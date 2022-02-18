from django.shortcuts import render
from .models import team
# Create your views here.

def Team(request):
    return render(request, 'team.html')