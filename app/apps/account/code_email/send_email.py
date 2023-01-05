from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from loguru import logger

from core import settings
from ..utils import AccountActivationTokenGenerator
from .redis_key import RedisKey


logger.add(
    "logs/users_logs.log",
    format="{time} {level} {message}",
    level="INFO",
    rotation="10MB",
    compression="zip"
)


class SendCodeEmail:
    @staticmethod
    def send_login_code(user : User) -> bool:
        assert user

        code = f'{urlsafe_base64_encode(force_bytes(user.id))}/' \
               f'{AccountActivationTokenGenerator().make_token(user)}'
        RedisKey().create_redis_key(code, user.id)

        context = {"code": code}
        message = render_to_string("account/email_code.html", context)
        subject = "Step Gym Formula: код для подтверждения вашей почты."

        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                auth_user=settings.EMAIL_HOST_USER,
                auth_password=settings.EMAIL_HOST_PASSWORD,
                recipient_list=[str(user.email)],
                fail_silently=False,
                html_message=message,
            )
            return True
        except Exception as _ex:
            logger.error(
                f"Error when sending a message user-{user.email}. Error-{_ex}"
            )
        return False
