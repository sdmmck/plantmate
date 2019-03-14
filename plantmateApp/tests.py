from django.test import TestCase
from plantmateApp.models import Plant, Business, Comment
from django.core.urlresolvers import reverse
import datetime
from django.utils import timezone

def add_plant(name, latin_name, size, charactertistics, climate, light, room, pet, slug, url, picture, description):
    plant = Plant.objects.get_or_create(name=name, latin_name=latin_name)[0]
    plant.size = size
    plant.charactertistics = charactertistics
    plant.climate = climate
    plant.light = light
    plant.room = room
    plant.pet = pet
    plant.slug = slug
    plant.url = url
    plant.picture = picture
    plant.description = description
    plant.save()
    return plant

class PlantTests(TestCase):
    def test_slug_line_creation(self):
        plant = Plant(name='Plant Name String')
        plant.save()

        self.assertEqual(plant.slug, 'plant-name-string')

class BusinessViewTests(TestCase):

    def test_business_view_with_no_businesses(self):
        """
        If no businesses exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('business-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No businesses currently to show.")
        self.assertQuerysetEqual(response.context['businesses'], [])

class IndexViewTests(TestCase):
    def test_plant_view(self):
        add_plant('hi', 'hi', 'small', 'hanging', 'hot', 'sunny', 'kitchen', 'no', 'slug', 'url', 'picture', 'description')

        response = self.client.get(reverse('plant'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "hi")

        num_plants =len(response.context['plants'])

        self.assertEqual(num_plants, 1)

