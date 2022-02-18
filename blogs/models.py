from django.db import models

# Create your models here.
class blog_details(models.Model):
    image=models.FileField(upload_to='image')
    content=models.CharField(max_length=50)
    title=models.CharField(max_length=50)
    published_date=models.DateField()

    def __str__(self):
        return self.title