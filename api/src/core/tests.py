from django.test import TestCase

# from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework import status


class MyTest(TestCase):
    def test_welcome(self):
        # Create your tests here.
        client = APIClient()
        response = client.get('/', None, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.logout()
