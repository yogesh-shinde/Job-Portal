from django import forms
from UserApp.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    conform_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['name', 'username', 'password',
                  'conform_password', 'address', 'contact', 'resume']
