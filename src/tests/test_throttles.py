from rest_framework import status
from .base import BaseAccountTest
from django.test import override_settings

@override_settings(
    CACHES={
        'default': {
            'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
            'LOCATION': 'throttle-test',
        }
    }
)

class ThrottleTests(BaseAccountTest):
    def test_throttle_on_change_status(self):
        self.authenticate(user=self.user)
        for i in range(12):
            if i % 2 == 0:
                response = self.client.post(f'/accounts/{self.active_account.id}/deactivate/')
                print(f'Throttle test deactivate attempt {i+1} \n', response.status_code, '\n', response.data)
            else:
                response = self.client.post(f'/accounts/{self.active_account.id}/activate/')
                print(f'Throttle test activate attempt {i+1} \n', response.status_code, '\n', response.data)

        response = self.client.post(f'/accounts/{self.active_account.id}/deactivate/')
        print('last one \n', response.status_code, '\n', response.data)