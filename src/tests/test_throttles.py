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
        for i in range(5):
            if i % 2 == 0:
                self.client.post(f'/accounts/{self.active_account.id}/deactivate/')
                # print(f'Throttle test deactivate attempt {i+1} \n', response.status_code, '\n', response.data)
            else:
                self.client.post(f'/accounts/{self.active_account.id}/activate/')
                # print(f'Throttle test activate attempt {i+1} \n', response.status_code, '\n', response.data)

        response = self.client.post(f'/accounts/{self.active_account.id}/activate/')
        print('last one \n', response.status_code, '\n', response.data)
        self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)

    def test_authenticated_user_throttle(self):
        self.authenticate(user=self.user)
        for i in range(200):
            self.client.get('/accounts/')
        response = self.client.get('/accounts/')
        print('out of loop request =>', response.status_code, response.data)
            # print(f'Authenticated user throttle test attempt {i+1} \n', response.status_code)

            # self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_429_TOO_MANY_REQUESTS])
        #     if response.status_code == status.HTTP_429_TOO_MANY_REQUESTS:
        #         break
        # self.assertEqual(response.status_code, status.HTTP_429_TOO_MANY_REQUESTS)