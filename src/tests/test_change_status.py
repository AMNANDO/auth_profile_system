from rest_framework import status
from .base import BaseAccountTest

class ChangeStatusTest(BaseAccountTest):
    def test_change_status(self):
        self.authenticate(user=self.user)
        response = self.client.post(f'/accounts/{self.active_account.id}/deactivate/')
        print('test change status to deactive \n', response.status_code, '\n', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        response = self.client.post(f'/accounts/{self.active_account.id}/activate/')
        print('test change status to active \n', response.status_code, '\n', response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
