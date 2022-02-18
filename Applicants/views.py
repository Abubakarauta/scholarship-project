from django.shortcuts import render
from .models import  applicant 
# Create your views here.





def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')



def applicant_details(request, id):
    detail=applicant.objects.get(id=id)
    context={
        'detail':detail
    }
    return render(request, 'applicant_details.html', context)

def applicants_list(request):
    user = applicant.objects.all()
    context={
        'user':user
    }

    return render(request, 'applicants_list.html',context)






