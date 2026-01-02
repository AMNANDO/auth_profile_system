from rest_framework import status
from .base import BaseAccountTest

class AccountListTest(BaseAccountTest):
    def test_authenticated_user_can_list_accounts(self):
        self.authenticate(user=self.user)
        response = self.client.get('/accounts/')
        print('test account list \n', response.status_code, '\n', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertTrue(response.data['success'])
        self.assertGreaterEqual(len(response.data['results']), 1)

