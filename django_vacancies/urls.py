"""django_vacancies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from vacancies.views import *
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('vacancies/<int:vacancy_id>', vacancy_view, name='vacancy'),
    path('companies/<int:company_id>', company_view, name='companies'),
    path('vacancies/', vacancies_view, name='all_vacancies'),
    path('', main_view, name='all_vacancies'),
    path('login', login_view.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', register_view, name='register'),
    path('vacancies/cat/<str:vacancies_path>', vacancies_view, name='vacancies_cat'),
    path('mycompany/letsstart/', mycompany_letsstart_view, name='mycompany_letsstart'),
    path('mycompany/create/', mycompany_edit_view, {'new': True}, name='mycompany_create'),
    path('mycompany', mycompany_edit_view, {'new': False}, name='mycompany_edit'),
    path('mycompany/vacancies/', mycompany_vacancies_view.as_view(), name='mycompany_vacancies'),
    path('mycompany/vacancies/create/', mycompany_vacancy_create_view, {'new': True}, name='mycompany_vacancy_create'),
    path('mycompany/vacancies/<int:vacancy_id>', mycompany_vacancy_create_view, {'new': False}, name='mycompany_vacancy'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)