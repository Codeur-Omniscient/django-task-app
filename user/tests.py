from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase


class RegisterTest(APITestCase):
    def test_register(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user']['username'], 'testuser')
        self.assertEqual(response.data['user']['email'], 'testuser@example.com')
        self.assertTrue('token' in response.data)


class LoginTest(APITestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )

    
    def test_login(self):
        url = reverse('login')
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)


class LogoutTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.token = Token.objects.get(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
    
    def test_logout(self):
        url = reverse('logout')
        response = self.client.post(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
