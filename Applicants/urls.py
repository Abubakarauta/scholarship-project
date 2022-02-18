
from django.urls import path
from .views import index,about,service,contact,applicants_list,applicant_details


urlpatterns = [
    path('', index , name='index'),
    path('applicants_list',applicants_list, name='applicants_list'),
    path('<int:id>/applicant_details',applicant_details, name='applicant_details'),
    path('about/', about , name='about'),
    path('service/', service , name='service'),
  
    path('contact/', contact , name='contact'),
    
            
    
   
]