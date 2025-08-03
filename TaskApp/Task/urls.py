from django.contrib import admin
from django.urls import path 
from Task import views
urlspatterns=[
    path('Task',views.index,name=home)
]