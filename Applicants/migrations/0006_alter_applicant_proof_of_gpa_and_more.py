# Generated by Django 4.0.2 on 2022-02-09 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Applicants', '0005_blog_details_alter_applicant_proof_of_gpa_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='Proof_of_Gpa',
            field=models.FileField(upload_to='image'),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='Secondary_school_testimony',
            field=models.FileField(upload_to='image'),
        ),
        migrations.AlterField(
            model_name='blog_details',
            name='image',
            field=models.FileField(upload_to='image'),
        ),
    ]
