from rest_framework.exceptions import APIException
from rest_framework import status
from rest_framework.views import exception_handler

class InactiveAccountException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = 'This account is inactive and cannot perform this action.'
    default_code = 'inactive_account'
class AlreadyInactiveAccountException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'This account is already inactive.'
    default_code = 'already_inactive_account'

class AlreadyActiveAccountException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'This account is already active.'
    default_code = 'already_active_account'

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        customized_response = {
            'success': False,
            'error': {
                'code': getattr(exc, 'default_code', 'error'),
                'details': response.data,
            }
        }
        response.data = customized_response

    return response