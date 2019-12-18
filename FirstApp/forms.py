from  django import forms
from FirstApp.models import Address,ITJobs,CIVILJobs,MECHJobs

class AddresForm(forms.ModelForm):
    class Meta:
        model = Address
        fields='__all__'
        

class ITJobsForm(forms.ModelForm):
    class Meta:
        model=ITJobs
        fields='__all__'
        exclude=['user']

class MECHJobsForm(forms.ModelForm):
    class Meta:
        model=MECHJobs
        fields='__all__'
        exclude=['user']

class CIVILJobsForm(forms.ModelForm):
    class Meta:
        model=CIVILJobs
        fields='__all__'
        exclude=['user']    