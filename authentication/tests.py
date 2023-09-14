from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User


class AccountTests(APITestCase):
    def test_create_account(self):
        url = reverse('auth_register')
        data = {
            "username": "Klaus",
            "password": "test123!",
            "password2": "test123!",
            "email": "test123@hot.de",
            "first_name": "Friedhelm",
            "last_name": "Test"
        }
        response = self.client.post(url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(User.objects.get().username, 'Klaus')
