from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Car


class ThingTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser1', password='pass')
        testuser1.save()

        test_car = Car.objects.create(owner=testuser1, name='BMW X4', description="Fast and Furious")
        test_car.save()

    def test_food_model(self):
        car = Car.objects.get(id=1)
        actual_owner = str(car.owner)
        actual_name = str(car.name)
        actual_description = str(car.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_name, "BMW X4")
        self.assertEqual(actual_description, "Fast and Furious")
