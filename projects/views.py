from django.shortcuts import render
from .models import  project

# Create your views here.

def PROJECT(request):
    projects = project.objects.all()
    context = {
        'projects':projects
    }
    return render(request, 'project.html',context)


