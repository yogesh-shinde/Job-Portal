from django.shortcuts import render, redirect,HttpResponse
from FirstApp.models import Address, ITJobs, MECHJobs, CIVILJobs
from FirstApp.forms import AddresForm, ITJobsForm, MECHJobsForm, CIVILJobsForm
from django.contrib.auth.decorators import login_required
from UserApp.forms import UserForm
from UserApp.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .decorators import user_login_required

# Create your views here.
@user_login_required
def user_dashboard(request):
    return render(request, 'UserApp/user_dashboard.html')

# Show IT Record
@user_login_required
def it_show(request):
    obj = ITJobs.objects.all()
    return render(request, 'UserApp/it_show.html', {'obj': obj})


# Show Mechanical Record
@user_login_required
def mech_show(request):
    obj=MECHJobs.objects.all()
    return render(request,'UserApp/mech_show.html',{'obj':obj})


# Show Civil Record
@user_login_required
def civil_show(request):
    obj=CIVILJobs.objects.all()
    return render(request,'UserApp/civil_show.html',{'obj':obj})

    
#User Login
def user_login(request):
    print(request)
    if(request.method == 'POST'):
        print("Post method")
        username=request.POST['txtuname']
        password=request.POST['txtpass']
        try:            
            user=User.objects.get(username=username,password=password)
            if(user is not None):
                print("Inside if ",user)
                request.session['user'] = user.username
                print("session set ", request.session['user'])
                return redirect('/userapp/user_dashboard/')
            else:
                messages.error(request,'Please enter valid username and password')
                return redirect('/userapp/user_login/')
        except(Exception):
            messages.error(request,'Please enter valid username and password')
            return redirect('/userapp/user_login/')
    return render(request,'UserApp/user_login.html')

#User Registration
def user_register(request):
    if(request.method == 'POST'):
        userform=UserForm(request.POST,request.FILES)
        if(userform.is_valid()):
            userform.save()
        return redirect('/userapp/user_login/')
    userform=UserForm()
    return render(request,'UserApp/user_register.html',{'userform':userform})

def it_apply(request):
    messages.success(request,'You are apply successfully, We will inform you by mail !!!')
    return redirect('/userapp/it_show/')

def mech_apply(request):
    messages.success(request,'You are apply successfully, We will inform you by mail !!!')
    return redirect('/userapp/mech_show/')

def civil_apply(request):
    messages.success(request,'You are apply successfully, We will inform you by mail !!!')
    return redirect('/userapp/civil_show/')