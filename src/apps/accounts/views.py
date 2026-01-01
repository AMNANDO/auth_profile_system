from os import access

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import action
from .models import Account
from .serializers import AccountSerializer
from .exceptions import (AlreadyInactiveAccountException,
                         AlreadyActiveAccountException,
                         InactiveAccountException)
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
# Create your views here.

class AccountsViewSet(ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user)

    def get_permissions(self):
        if self.action in ['retrieve', 'update', 'destroy', 'partial_update']:
            permissions =[IsAuthenticated, IsOwnerOrReadOnly]
        else:
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]


    def retrieve(self, request, *args, **kwargs):
        account = self.get_object()
        if not account.is_active:
            raise InactiveAccountException()
        serializer = self.get_serializer(account)
        return Response({
            'success': True,
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        account = self.get_object()
        if account.is_active:
            account.is_active = False
            account.save()
            return Response({
                'success': True,
                'message': 'Account has been deactivated.'
            }, status=status.HTTP_200_OK)
        raise AlreadyInactiveAccountException()

    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        account = self.get_object()
        if account.is_active:
            raise AlreadyActiveAccountException()
        account.is_active = True
        account.save()
        return Response({
            'success': True,
            'message': 'Account has been activated.'
        }, status=status.HTTP_200_OK)