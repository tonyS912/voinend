from django.urls import reverse
from django.test import TestCase, Client
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
            "email": "test@testomat.com",
            "first_name": "Friedhelm",
            "last_name": "Test"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.get().username, 'Klaus')


class LoginTest(TestCase):
    def test_login(self):
        self.client = Client()
        self.user = User.objects.create_user('test_user', email='test@testomat.com', password='test123!')
        self.client.login(email='test@testomat.com', password='test123!')

        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
