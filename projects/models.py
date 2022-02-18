from django.db import models

# Create your models here.

class project(models.Model):
    image=models.FileField(upload_to='image')
    name=models.CharField(max_length=50)
    content=models.CharField(max_length=50)
    published_date=models.DateTimeField()
    ending_date=models.DateTimeField()

    def __str__(self):
        return self.name