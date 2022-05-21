from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def signup(request):
    return HttpResponse("<p> sign up here</p>")
    
def login(request):
    return HttpResponse("<p> login</p>")