import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'plantmate.settings')
import django
django.setup()
from plantmateApp.models import Business, Plant


def populate():
    local_businesses = [
        {"title": "blooms",
         "url": "http://bloomsglasgow.co.uk/"},
        {"title": "Apercu",
         "url": "https://www.instagram.com/apercuglasgow/?hl=en"}
    ]
    plants = [
        {"name": "fern",
         "latin_name": "fernus mcfernface",
         "size": "medium",
         "characteristics": "trailing",
         "climate": "cool",
         "light": "sunny",
         "pet": "no"},
        {"name": "bullrush",
         "latin_name": "bullus rushus",
         "size": "large",
         "characteristics": "trailing",
         "climate": "warm",
         "light": "shady",
         "pet": "no"},
        {"name": "rubber plant",
         "latin_name": "ficus",
         "size": "large",
         "characteristics": "air purifying",
         "climate": "cool",
         "light": "shady",
         "pet": "no"}
    ]

    for business in local_businesses:
        add_business(business["title"], business["url"])

    for plant in plants:
        add_plant(plant)

    print(Business.objects.all())
    for c in Business.objects.all():
        print(c)


def add_business(title, url):
    p = Business.objects.get_or_create(name=title)[0]
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
                                        pet=plant["pet"])[0]
    plant.save()
    return plant


if __name__ == '__main__':
    print("Starting Plantmate population script...")
    populate()
