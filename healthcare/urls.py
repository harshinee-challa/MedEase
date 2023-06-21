from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('home/', views.index,name='index'),
    path('about/', views.about,name='about'),
    path('appointment/', views.appointment,name='apointment'),
    path('services/', views.services,name='services'),
]
