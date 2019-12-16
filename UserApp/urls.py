from django.urls import path
from UserApp import views

urlpatterns = [
    path('user_login/', views.user_login),
    path('user_register/', views.user_register),
    path('user_dashboard/', views.user_dashboard),
    path('it_apply/',views.it_apply),
    path('mech_apply/',views.mech_apply),
    path('civil_apply/',views.civil_apply),

    # IT URLS
    path('it_show/', views.it_show),
    path('it_add/', views.it_add),
    path('it_update/<int:id>/', views.it_update),
    path('it_delete/<int:id>/', views.it_delete),
    # MECH URLS
    path('mech_show/', views.mech_show),
    path('mech_add/', views.mech_add),
    path('mech_update/<int:id>/', views.mech_update),
    path('mech_delete/<int:id>/', views.mech_delete),
    # CIVIL URLS
    path('civil_show/', views.civil_show),
    path('civil_add/', views.civil_add),
    path('civil_update/<int:id>/', views.civil_update),
    path('civil_delete/<int:id>/', views.civil_delete),
]