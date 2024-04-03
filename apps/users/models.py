from core.constants import FieldLength
from core.models import TimeStamp
from django.contrib.auth.models import AbstractUser
from django.db import models


class RoleChoices(models.TextChoices):
    """Определение роли юзера."""

    ATTENDEE = ("attendee", "Участник")
    ORGANIZER = ("organizer", "Организатор")
    MODERATOR = ("moderator", "Модератор")


class CustomUser(AbstractUser, TimeStamp):
    """
    Кастомная модель переопределенного юзера.
    При создании пользователя все поля обязательны для заполнения.
    """

    email = models.EmailField(
        "Почта",
        unique=True,
        max_length=FieldLength.MAX_LENGTH_EMAIL.value,
    )
    password = models.CharField(
        "Пароль пользователя",
        max_length=FieldLength.MAX_LENGTH_PASSWORD.value,
    )
    first_name = models.CharField(
        "Имя пользователя",
        max_length=FieldLength.MAX_LENGTH_FIRST_NAME.value,
    )
    last_name = models.CharField(
        "Фамилия пользователя",
        max_length=FieldLength.MAX_LENGTH_LAST_NAME.value,
    )
    role = models.TextField(
        "Пользовательская роль",
        choices=RoleChoices.choices,
        default=RoleChoices.ATTENDEE,
        max_length=FieldLength.MAX_LENGTH_ROLE.value,
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["-id"]

    def __str__(self):
        return str(self.email)
