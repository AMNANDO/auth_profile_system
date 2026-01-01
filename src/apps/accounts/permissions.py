from rest_framework.permissions import BasePermission, SAFE_METHODS
class IsAccountActive(BasePermission):
    message = 'Account is inactive'
    def has_object_permission(self, request, view, obj):
        return obj.is_active

class IsOwner(BasePermission):
    message = 'you don`t own this account.'
    def has_object_permission(self, request, view, obj):
        if not obj.is_active:
            return False
        return obj.user == request.user

class IsAdmin(BasePermission):
    message = 'admin access required.'
    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_staff