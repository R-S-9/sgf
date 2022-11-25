from django.db import models


class ClientManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().select_related("user")


class Client(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    GENDER_CHOICES = (("M", "Муж"), ("F", "Жен"))
    gender = models.CharField(
        "Пол", max_length=1, choices=GENDER_CHOICES, blank=True
    )
    first_name = models.CharField("Имя", max_length=50)
    last_name = models.CharField("Фамилия", max_length=50)
    middle_name = models.CharField("Отчество", max_length=50, blank=True)
    birth_date = models.DateField("Дата рождения", blank=True, null=True)
    created = models.DateTimeField("Дата регистрации", auto_now_add=True)

    about_me = models.TextField(verbose_name='О себе')
    rank = models.CharField(
        verbose_name='Вид занятий',
        help_text='Пример: Тренер ТЗ, Персональный тренер, Тренер по боксу, '
                  'Инструктор групповых программ и тд.',
        max_length=150,
    )

    is_active = models.BooleanField(
        'Подтвержденный аккаутн', default=False
    )
    objects = ClientManager()

    def __str__(self):
        return f'{self.user.email} {self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподователи'
