from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def quiz(request):
    return HttpResponse("plantmate quiz")

def recommendations(request):
    return HttpResponse("recommendations")

def login(request):
    return HttpResponse("login save")

def signup(request):
    return HttpResponse("signup save")
  
def plant(request):
    return HttpResponse("This is a plant!")


def plantList(request):
    return HttpResponse("This is a list of plants!")






