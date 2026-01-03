from os import access

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiResponse
from .models import Account
from .serializers import AccountSerializer
from .throttles import (ChangeAccountStatusThrottle,
                        HourlyUserThrottle,
                        HourlyAnonRateThrottle)
from .exceptions import (AlreadyInactiveAccountException,
                         AlreadyActiveAccountException,
                         InactiveAccountException)
from .permissions import (IsOwner,
                          IsAdmin,
                          IsAccountActive)
from .pagination import AccountPagination
# Create your views here.

class AccountsViewSet(ModelViewSet):
    serializer_class = AccountSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = AccountPagination
    throttle_classes = [HourlyUserThrottle, HourlyAnonRateThrottle]
    filter_backends = (DjangoFilterBackend,
                       OrderingFilter,
                       SearchFilter)
    throttle_scope = 'account'
    filterset_fields = ['is_active', 'age', 'email', 'user']
    ordering_fields = ['age', 'name', 'created_at']
    search_fields = ['name', 'email', 'bio']
    ordering = ('-created_at',)

    def get_queryset(self):
        return Account.objects.select_related('user').all()

    def get_permissions(self):
        if self.action == 'retrieve':
            permissions = [IsAuthenticated, IsAccountActive, IsOwner]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permissions = [IsAuthenticated, IsAccountActive, IsOwner]
        elif self.action in ['deactivate', 'activate']:
            permissions = [IsAuthenticated, IsOwner]
        else :
            permissions = [IsAuthenticated]
        return [permission() for permission in permissions]


    def retrieve(self, request, *args, **kwargs):
        account = self.get_object()
        serializer = self.get_serializer(account)
        return Response({
            'success': True,
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    @extend_schema(
        description='Deactivate an active account.',
        responses={
            200: OpenApiResponse(
                description='Account successfully deactivated.'
            ),
            400: OpenApiResponse(
                description='Account already inactive'
            ),
            429: OpenApiResponse(
                description='Too many requests'
            )
        })

    @action(detail=True, methods=['post'], throttle_classes=[ChangeAccountStatusThrottle])
    def deactivate(self, request, pk=None):
        # self.throttle_scope = 'change_account_status'
        account = self.get_object()
        if account.is_active:
            account.is_active = False
            account.save()
            return Response({
                'success': True,
                'message': 'Account has been deactivated.'
            }, status=status.HTTP_200_OK)
        raise AlreadyInactiveAccountException()

    @extend_schema(
        description='Activate an inactive account.',
        responses={
            200: OpenApiResponse(
                description='Account successfully activated.'
            ),
            400: OpenApiResponse(
                description='Account already active'
            ),
            429: OpenApiResponse(
                description='Too many requests'
            )
        })

    @action(detail=True, methods=['post'], throttle_classes=[ChangeAccountStatusThrottle])
    def activate(self, request, pk=None):
        # self.throttle_scope = 'change_account_status'
        account = self.get_object()
        if account.is_active:
            raise AlreadyActiveAccountException()
        account.is_active = True
        account.save()
        return Response({
            'success': True,
            'message': 'Account has been activated.'
        }, status=status.HTTP_200_OK)