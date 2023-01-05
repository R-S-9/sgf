from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str

from loguru import logger
import six

from .code_email.redis_key import RedisKey


logger.add(
    "logs/users_logs.log",
    format="{time} {level} {message}",
    level="INFO",
    rotation="10MB",
    compression="zip"
)


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) +
            six.text_type(timestamp)  +
            six.text_type(user.is_active)
        )


class UserConfirmation:
    @staticmethod
    def user_confirmation(uidb64, token) -> bool:
        User = get_user_model()

        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
            user_id = RedisKey().get(f'{uidb64}/{token}').decode('utf-8')
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user, user_id = None, None

        if all([
            user,
            AccountActivationTokenGenerator().check_token(user, token),
            user_id
        ]):
            user.is_active = True
            user.save()

            logger.success(
                f"User-{user.email} activate account."
            )
            return True
        return False
