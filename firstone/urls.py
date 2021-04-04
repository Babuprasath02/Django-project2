from django.contrib import admin
from django.urls import path
from firstone import views

urlpatterns = [
    path('veh1', views.veh1),
    path('veh1/details/',views.getdb),
     ]
