from django.db import models

from apps.account.models import Teacher


class TrainingCourse(models.Model):
    EASY = 'EASY'
    MEDIUM = 'MEDIUM'
    HARD = 'HARD'

    user = models.ForeignKey(
        Teacher, verbose_name='Создатель курса', on_delete=models.CASCADE
    )
    name = models.CharField(
        verbose_name='Название курса', max_length=300,
    )
    description = models.TextField(
        verbose_name='О курсе', blank=True, null=True
    )
    # Для кого этот курс
    for_whom = models.TextField(
        verbose_name='Для кого курс', blank=True, null=True
    )
    # Начальные требования
    requirement = models.TextField(
        verbose_name='Начальные требования', blank=True, null=True
    )
    # Как проходит обучение
    learning_process = models.TextField(
        verbose_name='Процесс обучение', blank=True, null=True
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='Цена'
    )
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
    all_participant = models.PositiveIntegerField(
        verbose_name='Всего участников', default=0
    )
    main_image = models.ImageField(
        verbose_name='Главное изображение', blank=True, null=True
    )

    date_create = models.DateField('Дата создания', auto_now_add=True)
    modified = models.DateTimeField("Изменен", auto_now=True)

    def __str__(self):
        return f'Пользователь - {self.user.first_name} {self.user.last_name},'\
               f' курс - {self.name}, уровень - ' \
               f'{self.level_training in {self.EASY, self.MEDIUM, self.HARD}}'

    class Meta:
        verbose_name = 'Курс тренировок'
        verbose_name_plural = 'Курсы тренировок'


class CourseComposition(models.Model):
    """В курс входят. List"""
    course = models.ForeignKey(
        TrainingCourse, verbose_name='Курса', on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Кол-во контента', default=0
    )
    content_type = models.CharField(
        verbose_name='Тип контента',
        help_text='пример - урок,видео,текст и тд',
        max_length=100
    )

    def __str__(self):
        return f'Преподаватель - {self.course.user.first_name} ' \
               f'{self.course.user.last_name}, курс - {self.course.name}'

    class Meta:
        verbose_name = 'В курс входит'
        verbose_name_plural = 'В курс входят'


class CourseProgram(models.Model):
    """Программа курса. Полный список всех уроков"""

    chapter = models.CharField(
        verbose_name='Название главы', max_length=150
    )
    chapter_number = models.PositiveIntegerField(
        verbose_name='Глава номер',
        help_text='Строго следите за номером главы, т.к. по номеру формируется'
                  ' список курса',
    )

    class Meta:
        verbose_name = 'Программа курса'
        verbose_name_plural = 'Программы курса'


class Review(models.Model):
    """Отзывы"""
    review = models.TextField(
        verbose_name='Отзыв',
    )
    training_course_id = models.ForeignKey(
        TrainingCourse,
        verbose_name='Отзыв о курсе',
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    rating = models.IntegerField(
        verbose_name='Оценка',
    )
    date_create = models.DateTimeField('Дата создания', auto_now=True)
    order = models.IntegerField(
        verbose_name='Номер комментария',
        default=9999,
    )

    def _set_order(self):
        last_order = self.__class__.objects.filter(
            id_service_station=self.training_course_id
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
        return f'{self.training_course_id} {self.review}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        # unique_together = ('training_course_id', 'order')
        ordering = ('-order',)
