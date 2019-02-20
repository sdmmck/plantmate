from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def plant(request):
    return HttpResponse("This is a plant!")

def login(request):
    return HttpResponse("This is the login page")

def signup(request):
    return HttpResponse("This is the signup page")

def contact(request):
    return HttpResponse("This is the contact page")

def myaccount(request):
    return HttpResponse("This is your account page")








