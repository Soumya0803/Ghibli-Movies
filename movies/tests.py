from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

class MovieAPITests(APITestCase):

    def setUp(self):
        # Create a user and token for testing
        self.user = User.objects.create_user(username='test', password='test')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='ghiblikey ' + self.token.key)

    def test_get_movies_authenticated(self):
        # Test to get movies when authenticated
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_movies_unauthenticated(self):
        # Test to get movies without authentication
        self.client.force_authenticate(user=None)
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_movie_list_view(self):
        response = self.client.get(reverse('movie_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
