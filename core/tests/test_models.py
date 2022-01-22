from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email(self):
        """Test creating a new user with email"""
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

    def test_new_user_email_normalized(self):
        """Test the new email address(domain apart) for new user is normalized"""
        email = "Test@DOMAIN.COM"
        user = get_user_model().objects.create_user(
            email=email,
            password="test123",
        )
        # test
        email_separated = email.split("@")
        email = [email_separated[0]] + ["@"] + [email_separated[1].lower()]
        self.assertEqual(user.email, "".join(email))

    def test_new_user_invalid_email(self):
        """Test error when user is created without email"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")
