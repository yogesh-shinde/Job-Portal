from django.urls import path
from UserApp import views

urlpatterns = [
    path('user_login/', views.user_login),
    path('user_register/', views.user_register),
    path('user_dashboard/', views.user_dashboard),
    path('it_apply/<int:id>/', views.it_apply),
    path('mech_apply/<int:id>/', views.mech_apply),
    path('civil_apply/<int:id>/', views.civil_apply),
    path('user_profile/', views.user_profile),

    # IT URLS
    path('it_show/', views.it_show),

    # MECH URLS
    path('mech_show/', views.mech_show),

    # CIVIL URLS
    path('civil_show/', views.civil_show),
]
