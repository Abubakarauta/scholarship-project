from django.db import models

# Create your models here.
class applicant(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name= models.CharField(max_length=50)
    gender_choice = (
        ('male','Male'),
        ('female','Female')
    )
    Gender= models.CharField(max_length=7, choices=gender_choice, default='male')
    Email= models.CharField(max_length=50)
    School= models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    Phone_no = models.CharField(max_length=50)
    Registration_no = models.CharField(max_length=50)
    Date_Of_Birth = models.DateField(max_length=50)
    Year_of_Admission = models.IntegerField()
    Year_of_Graduation = models.IntegerField()
    Field_Of_study = models.CharField(max_length=50)
    Gpa_score = models.FloatField(max_length=50)
    Proof_of_Gpa = models.FileField( upload_to='image')
    Secondary_school_testimony = models.FileField(upload_to='image')
    Candidate_image = models.FileField(max_length=50)




    def __str__(self):
        return self.First_name





