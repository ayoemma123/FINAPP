from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.fill_form, name='fill_form'),
    
]
