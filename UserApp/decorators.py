from django.shortcuts import render, redirect
from django.http import HttpResponse


def user_login_required(function):
    def wrap(request):
        # print(request.session.get('user'))
        if request.session.get('user'):
            return function(request)
        else:
            return redirect('/userapp/user_login')
    return wrap
