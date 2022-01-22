from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        # create admin user
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@domain.com",
            password="test123",
        )
        # login admin user
        self.client.force_login(self.admin_user)
        # create normal user
        self.user = get_user_model().objects.create_user(
            email="testuser@domain.com",
            password="test123",
            name="Test User FullName",
        )

    def test_user_list(self):
        """Test that users are listed on admin user page"""
        # generate url rather than hard coding it
        url = reverse("admin:core_user_changelist")
        # get response
        res = self.client.get(url)
        # test
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        # generate url rather than hard coding it
        url = reverse("admin:core_user_change", args=[self.user.id])
        # sample url -> /admin/core/user/1/change/ where 1 is user id
        res = self.client.get(url)
        # test
        self.assertEqual(res.status_code, 200)

    def test_user_create_page(self):
        """Test that the user create page works"""
        # generate url rather than hard coding it
        url = reverse("admin:core_user_add")
        res = self.client.get(url)
        # test
        self.assertEqual(res.status_code, 200)
