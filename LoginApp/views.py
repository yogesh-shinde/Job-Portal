from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    if request.method == 'POST':
        obj = UserCreationForm(request.POST)
        if(obj.is_valid()):
            obj.save()
            return redirect('/login/')
    obj = UserCreationForm()
    return render(request, 'register.html', {'obj': obj})


def welcome(request):
    return render(request, 'welcome.html')


def user_welcome(request):
    return render(request, 'user_welcome.html')


def home(request):
    return render(request, 'home.html')
