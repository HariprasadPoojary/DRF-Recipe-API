from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def create_sample_user(email="test@domain.com", password="test123", name="testName"):
    """Create sample user for tests"""

    return get_user_model().objects.create_user(email, password, name)


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

    def test_create_new_super_user(self):
        """Test creating a new SUPER user with email"""
        user = get_user_model().objects.create_superuser(
            "admin@domain.com",
            "test123",
        )
        # test
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=create_sample_user(),
            name="vegan",
        )
        # test
        self.assertEqual(str(tag), tag.name)
