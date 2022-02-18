from django.shortcuts import render
from .models import  blog_details 
# Create your views here.

def blog_single(request):
    return render(request, 'blog_single.html')
    
def blog(request):
    blogs = blog_details.objects.all()
    context={
        'blogs':blogs,
    }
    return render(request, 'blog.html', context)