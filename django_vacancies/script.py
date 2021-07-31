import os
from datetime import datetime
import django

os.environ['DJANGO_SETTINGS_MODULE'] = 'django_vacancies.settings'
django.setup()

from vacancies.models import Company
from vacancies.models import Specialty
from vacancies.models import Vacancy
from data import *
from django.contrib.auth.models import User

for i in specialties:
    if Specialty.objects.filter(code=i['code']).count() != 0:
        continue
    print(i)
    Specialty.objects.create(
        code=i['code'],
        title=i['title'],
        picture='speciality_images/specty_'+i['code']+'.png',
    )
for i in companies:
    if Company.objects.filter(id=i['id']).count() != 0:
        continue
    Company.objects.create(
        id=int(i['id']),
        name=i['title'],
        logo='company_images/'+i['logo'],
        location=i['location'],
        employee_count=i['employee_count'],
        description=i['description'],

    )

for i in jobs:
    if Vacancy.objects.filter(id=i['id']).count() != 0:
        continue
    Vacancy.objects.create(
        id=int(i['id']),
        specialty=Specialty.objects.get(code=i['specialty']),
        company=Company.objects.get(id=i['company']),
        published_at=datetime.strptime(i['posted'], '%Y-%m-%d'),
        salary_min=i['salary_from'],
        salary_max=i['salary_to'],
        skills=i['skills'],
        description=i['description'],
    )

