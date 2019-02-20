from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Home Page")

  
def plant(request):
    context_dict = {'boldmessage': "PLANT!"}
    return render(request,'plantmate/plant.html', context=context_dict)


def plant_list(request):
    context_dict = {'boldmessage': "A LIST OF PLANTS!"}
    return render(request, 'plantmate/plantlist.html', context=context_dict)


def wishlist(request):
    context_dict = {'boldmessage': "all of the plants I wish I had"}
    return render(request, 'plantmate/wishlist.html', context=context_dict)


def my_plants(request):
    context_dict = {'boldmessage': "all of the plants I already have"}
    return render(request, 'plantmate/myplants.html', context=context_dict)







