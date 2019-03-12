import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'plantmate.settings')
import django
django.setup()
from plantmateApp.models import Business, Plant


def populate():
    local_businesses = [
        {"title": "blooms",
         "url": "http://bloomsglasgow.co.uk/",
         "address": "182 Dumbarton Rd, Glasgow",
         "lat": "55.870668",
         "long": "-4.300317"},
        {"title": "Apercu",
         "url": "https://www.instagram.com/apercuglasgow/?hl=en",
         "address": "617 Pollokshaws Road, Glasgow",
         "lat": "55.837192",
         "long": "-4.269045"}
    ]
    plants = [
        {"name": "Aloe Vera",
         "latin_name": "Aloe barbadensis miller",
         "size": "small",
         "characteristics": "Air purifying",
         "climate": "cool",
         "light": "sunny",
         "picture": "images/aloe-vera.jpg",
         "pet": "no",
         "room": "Living-room/Bedroom"},

        {"name": "Banana Plant",
         "latin_name": "Musa tropicana",
         "size": "Large",
         "characteristics": "Air purifying",
         "climate": "cool",
         "light": "sunny",
         "picture": "images/banana-plant.jpg",
         "pet": "yes",
         "room": "Living-room/Bedroom"},

        {"name": "Cast Iron Plant",
         "latin_name": "Aspidistra",
         "size": "Medium",
         "characteristics": "Easy to care for",
         "climate": "cool",
         "light": "shady",
         "picture": "images/cast-iron-plant.jpg",
         "pet": "yes",
         "room": "Living-room/Bedroom"},

        {"name": "Rose Painted Calathea",
         "latin_name": "Calathea roseopticta Dottie",
         "size": "Small",
         "characteristics": "Air purifying",
         "climate": "warm",
         "light": "sunny",
         "picture": "images/rose-painted-calathea.jpg",
         "pet": "yes",
         "room": "Kitchen/Bathroom"},

        {"name": "Chinese Evergreen",
         "latin_name": "Aglaeonema Maria",
         "size": "Medium",
         "characteristics": "Air purifying",
         "climate": "warm",
         "light": "shady",
         "picture": "images/chinese-evergreen.jpg",
         "pet": "yes",
         "room": "Kitchen/Bathroom"},

        {"name": "Chinese Money Plant",
         "latin_name": "Pilea peperomioides",
         "size": "small",
         "characteristics": "Easy to care for",
         "climate": "warm",
         "light": "sunny",
         "picture": "images/chinese-money-plant.jpg",
         "pet": "yes",
         "room": "Living-room/Bedroom"},

        {"name": "Dragon Plant",
         "latin_name": "Dracaena fragrans Lemon Lime",
         "size": "Large",
         "characteristics": "Air purifying",
         "climate": "warm",
         "light": "bright",
         "picture": "images/dragon-plant.jpg",
         "pet": "no",
         "room": "Living-room/Bedroom"},

        {"name": "Golden Pothos",
         "latin_name": "Epipremnum aureum",
         "size": "Small",
         "characteristics": "Trailing",
         "climate": "warm",
         "light": "shady",
         "picture": "images/golden-pothos.jpg",
         "pet": "no",
         "room": "Living-room/Bedroom"},

        {"name": "Swiss Cheese Plant",
         "latin_name": "Monstera deliciosa",
         "size": "Medium",
         "characteristics": "Easy to care for",
         "climate": "warm",
         "light": "shady",
         "picture": "images/swiss-cheese-plant.jpg",
         "pet": "no",
         "room": "Kitchen/Bathroom"},

        {"name": "Rattlesnake Plant",
         "latin_name": "Calathea Lancifolia",
         "size": "Medium",
         "characteristics": "Easy to care for",
         "climate": "warm",
         "light": "sunny",
         "picture": "images/rattlesnake-plant.jpg",
         "pet": "yes",
         "room": "Kitchen/Bathroom"},

        {"name": "Straight-Cylindrical Snake Plant",
         "latin_name": "Sanseveieria cylindrica",
         "size": "Medium",
         "characteristics": "Easy to care for",
         "climate": "warm",
         "light": "shady",
         "picture": "images/straight-cylindrical-snake-plant.jpg",
         "pet": "no",
         "room": "Living-room/Bedroom"},

        {"name": "Spider Plant",
         "latin_name": "Clorophytum comosum",
         "size": "small",
         "characteristics": "Trailing",
         "climate": "cool",
         "light": "sunny",
         "picture": "images/spider-plant.jpg",
         "pet": "yes",
         "room": "Living-room/Bedroom"},

        {"name": "String of Hearts",
         "latin_name": "Ceropegia woodii",
         "size": "small",
         "characteristics": "Trailing",
         "climate": "warm",
         "light": "sunny",
         "picture": "images/string-of-hearts.jpg",
         "pet": "no",
         "room": "Kitchen/Bathroom"},

        {"name": "Money Tree",
         "latin_name": "Pachira aquatica",
         "size": "Large",
         "characteristics": "Air purifying",
         "climate": "warm",
         "light": "shady",
         "picture": "images/money-tree.jpg",
         "pet": "no",
         "room": "Living-room/Bedroom"},

        {"name": "Parlour Palm",
         "latin_name": "Chamaedorea elegans",
         "size": "Large",
         "characteristics": "Air purifying",
         "climate": "cool",
         "light": "shady",
         "picture": "images/parlour-palm.jpg",
         "pet": "yes",
         "room": "Living-room/Bedroom"},

        {"name": "Ponytail Palm",
         "latin_name": "Beaucarnea recurvata",
         "size": "Medium",
         "characteristics": "Air purifying",
         "climate": "warm",
         "light": "shady",
         "picture": "images/ponytail-palm.jpg",
         "pet": "yes",
         "room": "Living-room/Bedroom"},

        {"name": "Spineless Yucca",
         "latin_name": "Yucca elephantipes",
         "size": "Large",
         "characteristics": "Easy to care for",
         "climate": "warm",
         "light": "sunny",
         "picture": "images/spineless-yucca.jpg",
         "pet": "yes",
         "room": "Living-room/Bedroom"},

    ]

    for business in local_businesses:
        add_business(business["title"], business["url"], business["address"], business["lat"], business["long"])

    for plant in plants:
        add_plant(plant)


def add_business(title, url, address, lat, long):
    p = Business.objects.get_or_create(name=title,
                                       address=address,
                                       lat=lat,
                                       long=long)[0]
    p.url = url
    p.save()
    return p


def add_plant(plant):
    plant = Plant.objects.get_or_create(name=plant["name"],
                                        latin_name=plant["latin_name"],
                                        size=plant["size"],
                                        characteristics=plant["characteristics"],
                                        climate=plant["climate"],
                                        light=plant["light"],
                                        picture=plant["picture"],
                                        pet=plant["pet"],
                                        room=plant["room"],
                                        )[0]
    plant.save()
    return plant


if __name__ == '__main__':
    print("Starting Plantmate population script...")
    populate()
