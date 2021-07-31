from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.http import HttpResponseRedirect

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'password')




def register_view(request):
    if request.method.upper() == 'POST':
        data = NewsletterForm(request.POST)
        if data.is_valid():
            User.objects.create_user(**data.cleaned_data)
            return HttpResponseRedirect('login')
        else:
            print(data.errors)
        return (render(request, 'register/register.html', {'NewsletterForm': data}))
    return(render(request, 'register/register.html',{'NewsletterForm': NewsletterForm}))

class login_view(LoginView):
    redirect_authenticated_user = True
    template_name = 'login/login.html'

