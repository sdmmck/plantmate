from django.test import TestCase
from django.test.client import Client
from plantmateApp.models import Plant, Business, Comment
from django.core.urlresolvers import reverse
from django.utils import timezone
import datetime
from plantmateApp.forms import CommentForm

class PlantModelTest(TestCase):

    def test_slug_line_creation(self):
        """
        checks that plant slugs are generated correctly from plant name.
        """
        plant = Plant(name='Rose Painted Calathea')
        plant.save()
        self.assertEqual(plant.slug, 'rose-painted-calathea')

class CommentModelTests(TestCase):

    def test_was_comment_published_recently_future_comment(self):
        """
        recently_published() returns False for questions whose created_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=12)
        future_comment = Comment(created_date=time)
        self.assertIs(future_comment.recently_published(), False)
    
    def test_was_comment_published_recently_old_comment(self):
        """
        recently_published() returns False for questions whose created_date
        is older than two days.
        """
        time = timezone.now() - datetime.timedelta(days=2, hours=1)
        old_comment = Comment(created_date=time)
        self.assertIs(old_comment.recently_published(), False)

    def test_was_comment_published_recently_recent_comment(self):
        """
        recently_published() returns True for questions whose created_date
        is less than two days.
        """

        time = timezone.now() - datetime.timedelta(days=1, hours=23, minutes=59, seconds=59)
        recent_comment = Comment(created_date=time)
        self.assertIs(recent_comment.recently_published(), True)

class BusinessTests(TestCase):

    def test_business_template_with_no_map(self):
        """
        If map fails, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('business-list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "map loading")
        self.assertQuerysetEqual(response.context['businesses'], [])

class CommentFormTests(TestCase):
   
    def test_valid_data(self):
        form = CommentForm({
            'plant_slug': "rose-painted-calathea",
            'body': "Hi there"
        })
        self.assertTrue(form.is_valid())
        comment = form.save()
        self.assertEqual(comment.plant_slug, "rose-painted-calathea")
        self.assertEqual(comment.body, "Hi there")
    
    def test_with_blank(self):
        form = CommentForm({})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors, {
            'plant_slug': ['This field is required.'],
            'body': ['This field is required.'],
        })

