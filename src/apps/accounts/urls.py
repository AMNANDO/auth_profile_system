from django.urls import path
from apps.accounts.views import AccountsViewSet
urlpatterns = [
    path('', AccountsViewSet.as_view({'get': 'list'})),
]