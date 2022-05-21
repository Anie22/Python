from turtle import home
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "home/index.html")

def about(request):
    return HttpResponse("<p>about</p>")    

def contact(request):
    return HttpResponse("<p>contact</p>")    
    