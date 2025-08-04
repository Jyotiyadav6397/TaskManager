from django.contrib import admin
from django.urls import path 
from Task import views
urlspatterns=[
    path('Task',views.index,name="index")
    path("home",veiws.home,name="home")
    path('about',views.about,name="about")
    path('tasks',views.tasks,name="tasks")
    path('profile',views.profile,name="profile")
    path('signup',views.signup,name="signup")
    
]