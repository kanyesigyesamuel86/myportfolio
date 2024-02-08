from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend
from django.core.exceptions import ObjectDoesNotExist

class OTPAuthenticationBackend(BaseBackend):
    def authenticate(self, request, email=None, otp=None):
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            if user.check_otp(otp):  # Implement a method to verify OTP
                return user
        except ObjectDoesNotExist:
            return None

    def get_user(self, user_id):
        User = get_user_model()
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
