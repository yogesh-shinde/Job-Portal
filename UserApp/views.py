from django.shortcuts import render, redirect, HttpResponse
from FirstApp.models import Address, ITJobs, MECHJobs, CIVILJobs
from FirstApp.forms import AddresForm, ITJobsForm, MECHJobsForm, CIVILJobsForm
from django.contrib.auth.decorators import login_required
from UserApp.forms import UserForm, UserProfile
from UserApp.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .decorators import user_login_required
from django.contrib.sessions.models import Session


# Create your views here.
@user_login_required
def user_dashboard(request,*args,**kwargs):
    return render(request, 'UserApp/user_dashboard.html')


# Show IT Record
@user_login_required
def it_show(request,*args,**kwargs):
    obj = ITJobs.objects.all()
    return render(request, 'UserApp/it_show.html', {'obj': obj})


# Show Mechanical Record
@user_login_required
def mech_show(request,*args,**kwargs):
    obj = MECHJobs.objects.all()
    return render(request, 'UserApp/mech_show.html', {'obj': obj})


# Show Civil Record
@user_login_required
def civil_show(request,*args,**kwargs):
    obj = CIVILJobs.objects.all()
    return render(request, 'UserApp/civil_show.html', {'obj': obj})


# User Login
def user_login(request):
    if (request.method == 'POST'):
        username = request.POST['txtuname']
        password = request.POST['txtpass']
        try:
            user = User.objects.get(username=username, password=password)
            print(user)
            if (user is not None):
                request.session['user'] = user.username
                request.session['user_id'] = user.id
                # print("session set id : ", request.session['user'])
                return redirect('/userapp/user_dashboard/')
            else:
                messages.error(request,
                               'Please enter valid username and password')
                return redirect('/userapp/user_login/')
        except (Exception):
            messages.error(request, 'Please enter valid username and password')
            return redirect('/userapp/user_login/')
    return render(request, 'UserApp/user_login.html')


# User Registration
def user_register(request):
    if (request.method == 'POST'):
        userform = UserForm(request.POST, request.FILES)
        if (userform.is_valid()):
            userform.save()
        return redirect('/userapp/user_login/')
    userform = UserForm()
    return render(request, 'UserApp/user_register.html',
                  {'userform': userform})

@user_login_required
def it_apply(request,*args,**kwargs):
    jobid=kwargs.get('id')
    if(jobid):
        messages.success(request, 'You are apply successfully, We will inform you by mail !!!')
        obj=ITJobs.objects.get(pk=jobid)
        user_id=request.session.get('user_id')
        uobj=User.objects.get(pk=user_id)
        obj.user.add(uobj)
        print(obj.user.all())
        obj.save()
        return redirect('/userapp/it_show/')
    return redirect('/userapp/it_show/')

@user_login_required
def mech_apply(request,*args,**kwargs):
    jobid=kwargs.get('id')
    if(jobid):
        messages.success(request, 'You are apply successfully, We will inform you by mail !!!')
        obj=MECHJobs.objects.get(pk=jobid)
        user_id=request.session.get('user_id')
        uobj=User.objects.get(pk=user_id)
        obj.user.add(uobj)
        print(obj.user.all())
        obj.save()
        return redirect('/userapp/mech_show/')
    return redirect('/userapp/mech_show/')

@user_login_required
def civil_apply(request,*args,**kwargs):
    jobid=kwargs.get('id')
    if(jobid):
        messages.success(request, 'You are apply successfully, We will inform you by mail !!!')
        obj=CIVILJobs.objects.get(pk=jobid)
        user_id=request.session.get('user_id')
        uobj=User.objects.get(pk=user_id)
        obj.user.add(uobj)
        print(obj.user.all())
        obj.save()
        return redirect('/userapp/civil_show/')
    return redirect('/userapp/civil_show/')


def user_profile(request):
    session_id = request.session.get('user_id')
    obj = User.objects.get(pk=session_id)
    if request.method == 'POST':
        userform = UserProfile(request.POST, request.FILES, instance=obj)
        if (userform.is_valid()):
            userform.save()
            return redirect('/userapp/user_dashboard/')
    userform = UserProfile(instance=obj)
    return render(request, 'UserApp/user_profile.html', {'userform': userform})
