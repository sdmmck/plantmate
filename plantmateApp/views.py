from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Home Page")

  
def plant(request):
    return HttpResponse("This is a plant!")


def plant_list(request):
    return HttpResponse("This is a list of plants!")


def wishlist(request):
    return HttpResponse("This is my wishlist of plants!")


def my_plants(request):
    return HttpResponse("This is a list of all of the plants that I own")







