from django.contrib.auth.backends import BaseBackend
from .models import CustomUser

class EmailBackend(BaseBackend):
    """
    Custom authentication backend for email-based login without passwords.
    """
    def authenticate(self, request, email=None, **kwargs):
        try:
            return CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None