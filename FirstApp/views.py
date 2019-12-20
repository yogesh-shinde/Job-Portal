from django.shortcuts import render, redirect
from FirstApp.models import Address, ITJobs, MECHJobs, CIVILJobs
from FirstApp.forms import AddresForm, ITJobsForm, MECHJobsForm, CIVILJobsForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'dashboard.html')

# Show IT Record
@login_required(login_url='/login/')
def it_show(request):
    obj = ITJobs.objects.all()
    return render(request, 'it_show.html', {'obj': obj})

# Add IT Record
@login_required(login_url='/login/')
def it_add(request):
    if (request.method == 'POST'):
        itform = ITJobsForm(request.POST)
        if (itform.is_valid()):
            itform.save()
        return redirect('/it_show/')

    itform = ITJobsForm()
    return render(request, 'it_add.html', {'itform': itform})

# Delete IT Record
@login_required(login_url='/login/')
def it_delete(request, id):
    obj = ITJobs.objects.get(pk=id)
    obj.delete()
    return redirect('/it_show/')

# Update IT Record
@login_required(login_url='/login/')
def it_update(request, id):
    obj = ITJobs.objects.get(pk=id)
    itform = ITJobsForm(instance=obj)
    if (request.method == 'POST'):
        itform = ITJobsForm(request.POST, instance=obj)
        if (itform.is_valid()):
            itform.save()
        return redirect('/it_show/')
    itform = ITJobsForm(instance=obj)
    return render(request, 'it_update.html', {'itform': itform, 'obj': obj})

# Show Mechanical Record
@login_required(login_url='/login/')
def mech_show(request):
    obj=MECHJobs.objects.all()
    return render(request,'mech_show.html',{'obj':obj})

# Add Mechanical Record
@login_required(login_url='/login/')
def mech_add(request):
    if(request.method == 'POST'):
        mechform=MECHJobsForm(request.POST)
        if(mechform.is_valid()):
            mechform.save()
        return redirect('/mech_show/')
    mechform=MECHJobsForm()
    return render(request,'mech_add.html',{'mechform':mechform})

# Delete Mechanical Record
@login_required(login_url='/login/')
def mech_delete(request,id):
    obj=MECHJobs.objects.get(pk=id)
    obj.delete()
    return redirect('/mech_show/')

# Update Mechanical Record
@login_required(login_url='/login/')
def mech_update(request,id):
    obj=MECHJobs.objects.get(pk=id)
    mechform=MECHJobsForm(instance=obj)
    if(request.method == 'POST'):
        mechform=MECHJobsForm(request.POST,instance=obj)
        if(mechform.is_valid()):
            mechform.save()
        return redirect('/mech_show/')
    mechform=MECHJobsForm(instance=obj)
    return render(request,'mech_update.html',{'mechform':mechform,'obj':obj})

# Show Civil Record
@login_required(login_url='/login/')
def civil_show(request):
    obj=CIVILJobs.objects.all()
    return render(request,'civil_show.html',{'obj':obj})

#Add Civil Record
@login_required(login_url='/login/')
def civil_add(request):
    if(request.method == 'POST'):
        civilform=CIVILJobsForm(request.POST)
        if(civilform.is_valid()):
            civilform.save()
        return redirect('/civil_show/')
    civilform=CIVILJobsForm()
    return render(request,'civil_add.html',{'civilform':civilform})

#Delete Civil Record
@login_required(login_url='/login/')
def civil_delete(request,id):
    obj=CIVILJobs.objects.get(pk=id)
    obj.delete()
    return redirect('/civil_show/')

#Update Civil Record
@login_required(login_url='/login/')
def civil_update(request,id):
    obj=CIVILJobs.objects.get(pk=id)
    civilform=CIVILJobsForm(instance=obj)
    if(request.method == 'POST'):
        civilform=CIVILJobsForm(request.POST,instance=obj)
        if(civilform.is_valid()):
            civilform.save()
        return redirect('/civil_show/')
    civilform=CIVILJobsForm(instance=obj)
    return render(request,'civil_update.html',{'obj':obj,'civilform':civilform})

# Show applied resume by user
def resume_it(request,id):
    itjobs=ITJobs.objects.get(pk=id)
    users=itjobs.user.all()
    return render(request,'apply_resume.html',{'user_resume':users})