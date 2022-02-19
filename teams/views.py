from django.shortcuts import render
from .models import team
# Create your views here.

def Team(request):
    teams=team.objects.all()
    context = {
        'teams':teams
    }
    return render(request, 'team.html',context)