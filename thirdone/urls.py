from django.contrib import admin
from django.urls import path
from thirdone import views

urlpatterns = [
    path('veh3', views.veh3),
    path('veh3/detailsc',views.getdb),
     ]
