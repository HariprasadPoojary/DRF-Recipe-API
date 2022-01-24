from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


CREATE_USER_URL = reverse("user:create")
TOKEN_URL = reverse("user:token")


def create_user(**kwargs):
    return get_user_model().objects.create_user(**kwargs)


class PublicUserApiTests(TestCase):
    """Test the users API(Public)"""

    def setUp(self) -> None:
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test create user with valid payload"""
        payload = {
            "email": "test@domain.com",
            "password": "test123",
            "name": "Test Name",
        }
        # send http post request & save response
        res = self.client.post(CREATE_USER_URL, payload)
        # get created user's info
        user = get_user_model().objects.get(**res.data)

        # ***** test
        # test status code
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        # test that password is hashed
        self.assertNotIn(payload["password"], res.data)
        # test that password matches
        self.assertTrue(user.check_password(payload["password"]))

    def test_duplicate_user(self):
        """Test creating user that already exists fails"""
        payload = {
            "email": "test_duplicate@domain.com",
            "password": "test123",
            "name": "Test DuplicateName",
        }
        # create a user
        create_user(**payload)
        # create user again, send http post request & save response
        res = self.client.post(CREATE_USER_URL, payload)
        # test that request is rejected
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_for_user(self):
        """Test that token is created for user"""
        payload = {
            "email": "test_token@domain.com",
            "password": "test123",
            "name": "Test tokenName",
        }
        # create a user
        create_user(**payload)
        # send post request to create token and save response
        res = self.client.post(TOKEN_URL, payload)
        # test if token is present in the response payload
        self.assertIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_token_invaid_credentials(self):
        """Test that token request is rejected for invalid credentials"""
        # create valid user
        valid_payload = {
            "email": "test_token@domain.com",
            "password": "test123",
            "name": "Test tokenName",
        }
        create_user(**valid_payload)
        # create incorrect payload
        invalid_payload = {
            "email": "test_token@domain.com",
            "password": "wrong_password",
            "name": "Test tokenName",
        }
        # send post request to create token and save response
        res = self.client.post(TOKEN_URL, invalid_payload)
        # test
        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        """Test that token request is rejected for invalid user"""
        # create incorrect payload
        invalid_payload = {
            "email": "test_token@domain.com",
            "password": "wrong_password",
            "name": "Test tokenName",
        }
        # send post request to create token and save response
        res = self.client.post(TOKEN_URL, invalid_payload)
        # test
        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_password(self):
        """Test that token request is rejected for missing password"""
        # create incorrect payload
        invalid_payload = {
            "email": "test_token@domain.com",
            "password": "",
            "name": "Test tokenName",
        }
        # send post request to create token and save response
        res = self.client.post(TOKEN_URL, invalid_payload)
        # test
        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
