from core.constants import FieldLenght
from core.models import TimeStamp
from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser, TimeStamp):
    """
    Кастомная модель переопределенного юзера.
    При создании пользователя все поля обязательны для заполнения.
    """

    class RoleChoises(models.TextChoices):
        """
        Определение роли юзера.
        """

        ATTENDEE = "attendee"
        ORGANIZER = "organizer"
        ADMIN = "admin"

    email = models.EmailField(
        "Почта",
        unique=True,
        max_length=FieldLenght.MAX_LENGHT_EMAIL.value,
    )
    password = models.CharField(
        "Пароль пользователя",
        max_length=FieldLenght.MAX_LENGHT_PASSWORD.value,
    )
    first_name = models.CharField(
        "Имя пользователя",
        max_length=FieldLenght.MAX_LENGHT_FIRST_NAME.value,
    )
    last_name = models.CharField(
        "Фамилия пользователя",
        max_length=FieldLenght.MAX_LENGHT_LAST_NAME.value,
    )
    role = models.TextField(
        "Пользовательская роль",
        choices=RoleChoises.choices,
        default=RoleChoises.ATTENDEE,
        max_length=FieldLenght.MAX_LENGHT_ROLE.value,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["-id"]

    def __str__(self):
        return str(self.email)
