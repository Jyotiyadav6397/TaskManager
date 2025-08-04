# from django.contrib import admin
# from django.urls import path,include 
# from Task import views
# urlspatterns=[
#     path('',views.index,name="index"),
    
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("home",views.home,name="home"),
    path('about',views.about,name="about"),
    path('tasks',views.tasks,name="tasks"),
    path('profile',views.profile,name="profile"),
    path('signup',views.signup,name="signup")
    
]
