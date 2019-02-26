import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import plantmateApp
plantmateApp.setup()
from plantmateApp.models import Business


def populate():
    local_businesses = [
        {"title": "blooms/",
         "url":"http://bloomsglasgow.co.uk/"},
        {"title":"Apercu",
         "url":"https://www.instagram.com/apercuglasgow/?hl=en"}]

    cats = {"Businesses": {"Local Businesses": local_businesses}}

    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data["Local Businesses"]:
            add_business(c, p["title"], p["url"])

    # Print out the categories we have added.
    for c in Business.objects.all():
            print("- {0} - {1}".format(str(c)))


def add_business(cat, title, url, views=0):
    p = Business.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return ppytho


def add_cat(name):
    c = Business.objects.get_or_create(name=name)[0]
    c.save()
    return c


if __name__ == '__main__':
    print("Starting Plantmate population script...")
    populate()
