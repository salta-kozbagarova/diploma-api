from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from auction_api.transports.models import Car

class CarTests(APITestCase):

    # def test_create_car(self):
    #     """
    #     Ensure we can create a new car object.
    #     """
    #     url = reverse('cars-list')
    #     data = {'name': 'DabApps'}
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    #     self.assertEqual(Car.objects.count(), 1)
    #     self.assertEqual(Car.objects.get().name, 'DabApps')

    def test_list_car(self):
        """
        Ensure we can create a new car object.
        """
        response = self.client.get('/cars/')
        self.assertEqual(response.data, [])
