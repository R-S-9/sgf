from django.core.mail import send_mail
from django.template.loader import render_to_string

from core import settings
from ..utils import ShortToken
from .redis_key import RedisKey


class SendCodeEmail:
    @staticmethod
    def send_login_code(user_id: int, user_email: str):
        assert user_id

        uuid_token = ShortToken.create_short_token()
        RedisKey().create_redis_key(uuid_token, user_id)

        context = {"code": uuid_token}
        message = render_to_string("account/email_code.html", context)
        subject = "Step Gym Formula: код для подтверждения вашей почты."

        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            auth_user=settings.EMAIL_HOST_USER,
            auth_password=settings.EMAIL_HOST_PASSWORD,
            recipient_list=[str(user_email)],
            fail_silently=False,
            html_message=message,
        )
