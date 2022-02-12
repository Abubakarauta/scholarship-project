
from django.urls import path
from .views import index,project,about,service,team,contact,blog_single,blog,applicants_list,applicant_details


urlpatterns = [
    path('', index , name='index'),
    path('applicants_list',applicants_list, name='applicants_list'),
    path('<int:id>/applicant_details',applicant_details, name='applicant_details'),
    path('project/', project , name='project'),
    path('about/', about , name='about'),
    path('service/', service , name='service'),
    path('team/', team , name='team'),
    path('contact/', contact , name='contact'),
    path('blog_single/', blog_single , name='blog_single'),
    path('blog/', blog , name='blog'),
            
    
   
]