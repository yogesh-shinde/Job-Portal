from django import forms
from UserApp.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    conform_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'username', 'password',
                  'conform_password', 'address', 'contact', 'resume']


class UserProfile(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
        exclude = ['password', 'conform_password']
