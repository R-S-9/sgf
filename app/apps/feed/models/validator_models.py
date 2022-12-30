from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_rating(rating):
    if rating > 5 or rating < 1:
        raise ValidationError(
            _('%(rating)s is not included in the range'),
            params={'rating': rating},
        )
