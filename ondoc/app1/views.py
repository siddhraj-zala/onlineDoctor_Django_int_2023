from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("HOME PAGE")

def aboutus(request):
    return render(request,"app1/aboutus.html")

def contactus(request):
    return render(request,"app1/contactus.html")

