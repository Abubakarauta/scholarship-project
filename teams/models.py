from django.db import models

# Create your models here.

class team(models.Model):
    name=models.CharField(max_length=50)
    role=models.CharField(max_length=50)
    image=models.FileField(upload_to='image')

    def __str__(self):
        return self.name