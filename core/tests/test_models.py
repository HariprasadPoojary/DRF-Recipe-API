from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email(self):
        """
        Test creating a new user with email
        """
        email = "test@domain.com"
        password = "test123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        # test user email
        self.assertEqual(user.email, email)
        # test user password
        self.assertTrue(user.check_password(password))
