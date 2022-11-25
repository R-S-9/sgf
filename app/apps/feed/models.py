from django.db import models


class TrainingCourses(models.Model):
    EASY = 'EASY'
    MEDIUM = 'MEDIUM'
    HARD = 'HARD'

    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(
        verbose_name='Название курса', max_length=300,
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    LEVEL_TRAINING = [
        (EASY, 'Easy'),
        (MEDIUM, 'Medium'),
        (HARD, 'Hard'),
    ]
    level_training = models.CharField(
        verbose_name='Уровень тяжести',
        max_length=6,
        choices=LEVEL_TRAINING,
        default=EASY,
    )

    date_create = models.DateField('Дата создания', auto_now_add=True)

    def __str__(self):
        # return f'user-{self.user.name} courses-{self.name} level-' \
        #     f'{self.level_training in {self.EASY, self.MEDIUM, self.HARD}}'
        return self.name

    class Meta:
        verbose_name = 'Курс тренировок'
        verbose_name_plural = 'Курсы тренировок'
