from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


# Create your tests here.
class UserRegistrationTest(APITestCase):
    def test_registration(self):
        url = reverse("user_view")
        user_data = {
            "username" : "testuser",
            "fullname" : "테스터",
            "email" : "test@testuser.com",
            "password" : "password",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.status_code, 200)