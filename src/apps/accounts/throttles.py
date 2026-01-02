from rest_framework.throttling import ScopedRateThrottle, SimpleRateThrottle, AnonRateThrottle

class HourlyUserThrottle(SimpleRateThrottle):
    scope = 'hourly_user'

    def get_cache_key(self, request, view):
        if not request.user.is_authenticated:
            return None  # Only throttle authenticated users

        return self.cache_format % {
            'scope': self.scope,
            'ident': request.user.pk
        }
class HourlyAnonRateThrottle(AnonRateThrottle):
    scope = 'hourly_anon'

    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            return None  # Only throttle anonymous users

        return super().get_cache_key(request, view)

class ChangeAccountStatusThrottle(SimpleRateThrottle):
    scope = 'change_account_status'

    def get_cache_key(self, request, view):
        if not request.user.is_authenticated:
            return None  # Only throttle authenticated users

        return f'change-status-{request.user.id}'