from django.contrib import admin
from django.urls import path
from vehicle import views

urlpatterns = [
    path('', views.task2),
     ]
