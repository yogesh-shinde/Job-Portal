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

# Add IT Record
@user_login_required
def it_add(request):
    if (request.method == 'POST'):
        itform = ITJobsForm(request.POST)
        if (itform.is_valid()):
            itform.save()
        return redirect('/userapp/it_show/')

    itform = ITJobsForm()
    return render(request, 'UserApp/it_add.html', {'itform': itform})

# Delete IT Record
@user_login_required
def it_delete(request, id):
    obj = ITJobs.objects.get(pk=id)
    obj.delete()
    return redirect('/userapp/it_show/')

# Update IT Record
@user_login_required
def it_update(request, id):
    obj = ITJobs.objects.get(pk=id)
    itform = ITJobsForm(instance=obj)
    if (request.method == 'POST'):
        itform = ITJobsForm(request.POST, instance=obj)
        if (itform.is_valid()):
            itform.save()
        return redirect('/userapp/it_show/')
    itform = ITJobsForm(instance=obj)
    return render(request, 'UserApp/it_update.html', {'itform': itform, 'obj': obj})

# Show Mechanical Record
@user_login_required
def mech_show(request):
    obj=MECHJobs.objects.all()
    return render(request,'UserApp/mech_show.html',{'obj':obj})

# Add Mechanical Record
@user_login_required
def mech_add(request):
    if(request.method == 'POST'):
        mechform=MECHJobsForm(request.POST)
        if(mechform.is_valid()):
            mechform.save()
        return redirect('/userapp/mech_show/')
    mechform=MECHJobsForm()
    return render(request,'UserApp/mech_add.html',{'mechform':mechform})

# Delete Mechanical Record
@user_login_required
def mech_delete(request,id):
    obj=MECHJobs.objects.get(pk=id)
    obj.delete()
    return redirect('/userapp/mech_show/')

# Update Mechanical Record
@user_login_required
def mech_update(request,id):
    obj=MECHJobs.objects.get(pk=id)
    mechform=MECHJobsForm(instance=obj)
    if(request.method == 'POST'):
        mechform=MECHJobsForm(request.POST,instance=obj)
        if(mechform.is_valid()):
            mechform.save()
        return redirect('/userapp/mech_show/')
    mechform=MECHJobsForm(instance=obj)
    return render(request,'UserApp/mech_update.html',{'mechform':mechform,'obj':obj})

# Show Civil Record
@user_login_required
def civil_show(request):
    obj=CIVILJobs.objects.all()
    return render(request,'UserApp/civil_show.html',{'obj':obj})

#Add Civil Record
@user_login_required
def civil_add(request):
    if(request.method == 'POST'):
        civilform=CIVILJobsForm(request.POST)
        if(civilform.is_valid()):
            civilform.save()
        return redirect('/userapp/civil_show/')
    civilform=CIVILJobsForm()
    return render(request,'UserApp/civil_add.html',{'civilform':civilform})

#Delete Civil Record
@user_login_required
def civil_delete(request,id):
    obj=CIVILJobs.objects.get(pk=id)
    obj.delete()
    return redirect('/userapp/civil_show/')

#Update Civil Record
@user_login_required
def civil_update(request,id):
    obj=CIVILJobs.objects.get(pk=id)
    civilform=CIVILJobsForm(instance=obj)
    if(request.method == 'POST'):
        civilform=CIVILJobsForm(request.POST,instance=obj)
        if(civilform.is_valid()):
            civilform.save()
        return redirect('/userapp/civil_show/')
    civilform=CIVILJobsForm(instance=obj)
    return render(request,'UserApp/civil_update.html',{'obj':obj,'civilform':civilform})
    
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