from django.contrib import admin
from vacancies.models import Company
from vacancies.models import Specialty
from vacancies.models import Vacancy

class bCompany(admin.ModelAdmin):
    pass


class bSpecialty(admin.ModelAdmin):
    pass

class bVacancy(admin.ModelAdmin):
    pass


admin.site.register(Company, bCompany)
admin.site.register(Specialty, bSpecialty)
admin.site.register(Vacancy, bVacancy)
