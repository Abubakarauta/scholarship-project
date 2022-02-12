from django.shortcuts import render
from .models import  applicant, blog_details 
# Create your views here.





def index(request):
    return render(request, 'index.html')

def project(request):
    return render(request, 'project.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def team(request):
    return render(request, 'team.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    blogs = blog_details.objects.all()
    context={
        'blogs':blogs,
    }
    return render(request, 'blog.html', context)

def blog_single(request):
    return render(request, 'blog_single.html')

def applicant_details(request, id):
    detail=applicant.objects.get(id=id)
    context={
        'detail':detail
    }
    return render(request, 'applicant_details.html', context)

def applicants_list(request):
    user=applicant.objects.all()
    context={
        'user':user
    }

    return render(request, 'applicants_list.html',context)