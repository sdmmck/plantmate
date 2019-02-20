from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

  
def plant(request):
    return HttpResponse("This is a plant!")


def plantList(request):
    return HttpResponse("This is a list of plants!")






