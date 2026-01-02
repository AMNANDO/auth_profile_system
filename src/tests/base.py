from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from apps.accounts.models import Account

class BaseAccountTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a test user
        cls.user = User.objects.create_user(username='whoami', password='adminnistam')
        # Create admin user
        cls.admin = User.objects.create_superuser(username='admin', password='adminadmin')
        # Create a test account linked to the user
        cls.active_account = Account.objects.create(
            # id=1,
            user=cls.user,
            name='Test User',
            age=30,
            bio='This is a test user.',
            email='activeuser@gmail.com',
            is_active=True,
        )
        # cls.inactive_account = Account.objects.create(
        #     # id=2,
        #     user=cls.user,
        #     name='Inactive User',
        #     age=25,
        #     bio='This is an inactive user.',
        #     email='inActiveUser@gmail.com',
        #     is_active=False,
        # )
    def authenticate(self, user):
        self.client.force_authenticate(user=user)