from django.urls import path
from LoginApp import views
urlpatterns = [
    path('register/', views.register),
    path('welcome/', views.welcome),
    path('userwelcome/', views.user_welcome),
    path('home/', views.home),

]
