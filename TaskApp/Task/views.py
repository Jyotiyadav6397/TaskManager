from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is home page")
   return render(request,"index.html")
def home(request):
    # return HttpResponse("This is home page")
   return render(request,"home.html")

def about(request):
    # return HttpResponse("This is home page")
   return render(request,"about.html")

def tasks(request):
    # return HttpResponse("This is home page")
   return render(request,"tasks.html")   

def profile(request):
    # return HttpResponse("This is home page")
   return render(request,"profile.html")   

def signup(request):
    # return HttpResponse("This is home page")
   return render(request,"signup.html")