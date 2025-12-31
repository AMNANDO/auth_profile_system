from django.shortcuts import render
from rest_framework import response , viewsets
# Create your views here.

class AccountsViewSet(viewsets.ModelViewSet):
    def list(self, request, *args, **kwargs):
        return response.Response({"message": "Hello, this is the Accounts viewset!"})
