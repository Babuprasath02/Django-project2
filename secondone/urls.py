from django.contrib import admin
from django.urls import path
from secondone import views

urlpatterns = [
    path('veh2', views.veh2),
    path('veh2/detailsb',views.getdb),
     ]
