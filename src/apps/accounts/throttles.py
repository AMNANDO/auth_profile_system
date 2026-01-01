from rest_framework.throttling import ScopedRateThrottle

class ChangeAccountStatusThrottle(ScopedRateThrottle):
    scope = 'change_account_status'