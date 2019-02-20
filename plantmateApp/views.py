from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

def quiz(request):
    return HttpResponse("plantmate quiz")