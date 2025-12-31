from django.urls import path
from .views import AccountsViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'accounts', AccountsViewSet, basename='accounts')

urlpatterns = router.urls