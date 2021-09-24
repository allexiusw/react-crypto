from django.test import TestCase
from django.urls import reverse
from core.models import Account

# from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class MyTest(TestCase):
    def test_welcome(self):
        client = APIClient()
        response = client.get('/', None, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        client.logout()


class DjoserTest(APITestCase):
    '''Test djoser API'''
    def test_create_account(self):
        """Ensure we can create a new account object."""
        url = reverse('account-list')
        data = {'name': 'DabApps'}
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Account.objects.count(), 0)
