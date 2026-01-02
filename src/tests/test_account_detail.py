from rest_framework import status
from .base import BaseAccountTest

class AccountRetrieveTest(BaseAccountTest):
    def test_owner_can_retrieve_own_account(self):
        self.authenticate(user=self.user)
        response = self.client.get(f'/accounts/{self.active_account.id}/')
        print('test account retrieve \n', response.status_code, '\n', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])

    def test_another_user_cannot_retrieve_account(self):
        self.authenticate(user=self.another_user)
        response = self.client.get(f'/accounts/{self.active_account.id}/')
        print('test another user retrieve account \n', response.status_code, '\n', response.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # self.assertFalse(response.data['success'])