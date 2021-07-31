from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from datetime import datetime


class Company(models.Model):
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company_images/', blank=True, null=True)
    description = models.TextField()
    employee_count = models.IntegerField()
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Company')

    class Meta:
        app_label = 'vacancies'


class Specialty(models.Model):
    code = models.CharField(max_length=15)
    title = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='speciality_images/')

    class Meta:
        app_label = 'vacancies'


class Vacancy(models.Model):
    title = models.CharField(max_length=20)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.TextField()
    description = models.TextField()
    salary_min = models.FloatField()
    salary_max = models.FloatField()
    published_at = models.DateField(default=datetime.now())

    class Meta:
        app_label = 'vacancies'


class Application(models.Model):
    written_username = models.CharField(max_length=20)
    written_phone = models.CharField(max_length=20)
    written_cover_letter = models.TextField()
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
