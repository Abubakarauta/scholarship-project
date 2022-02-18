
from django.urls import path
from .views import blog_single,blog

urlpatterns = [
    
    path('blog_single/', blog_single , name='blog_single'),
    path('blog/', blog , name='blog'),
            
    
   
]