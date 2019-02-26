import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'plantmate.settings')

import django
django.setup()
from plantmateApp.models import Business


def populate():
    local_businesses = [
        {"title": "blooms",
         "url": "http://bloomsglasgow.co.uk/"},
        {"title": "Apercu",
         "url": "https://www.instagram.com/apercuglasgow/?hl=en"},]

    for cat_data in local_businesses:
        add_business(cat_data["title"], cat_data["url"])

    print(Business.objects.all())
    for c in Business.objects.all():
        print(c)


def add_business(title, url):
    p = Business.objects.get_or_create(name=title)[0]
    p.url = url
    p.save()
    return p


if __name__ == '__main__':
    print("Starting Plantmate population script...")
    populate()
