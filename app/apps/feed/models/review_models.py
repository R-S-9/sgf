from django.db import models

from .course_models import TrainingCourse
from .validator_models import validate_rating


class Review(models.Model):
    """Отзывы"""
    user = models.OneToOneField(
        "auth.User", verbose_name='Пользователь', on_delete=models.CASCADE
    )
    review = models.TextField(
        verbose_name='Отзыв',
    )
    training_course_id = models.ForeignKey(
        TrainingCourse,
        verbose_name='Курс',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.SmallIntegerField(
        verbose_name='Оценка',
        help_text="Диапазон от 1 до 5(!)",
        validators=[validate_rating]
    )
    date_create = models.DateTimeField('Дата создания', auto_now=True)
    order = models.IntegerField(
        verbose_name='Номер комментария',
        default=9999999,
    )

    def _set_order(self):
        last_order = self.__class__.objects.filter(
            training_course_id=self.training_course_id
        ).order_by('order').values_list(
            'order', flat=True
        ).last()

        if last_order:
            self.order = last_order + 1
        else:
            self.order = 1

    def save(self, *args, **kwargs):
        self._set_order()
        super(Review, self).save(*args, **kwargs)

    def __str__(self):
        return f'Курс {self.training_course_id.name}, отзыв {self.review}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        # unique_together = ('training_course_id', 'order')
        ordering = ('-order',)
