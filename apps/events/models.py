from django.db import models

from apps.users.models import CustomUser
from apps.core.constants import MAX_LENGTH_REGISTRATION_STAGE


class RegistrationStageChoices(models.TextChoices):
    """Стадия регистрации на мероприятие"""
    PARTICIPATED = ("participated", "Участвовал")
    PARTICIPATING = ("participating", "Участвую")
    NOT_REGISTERED = ("Not_registered", "Не зарегистрирован")


class Registration(models.Model):
    """Модель регистрации на мероприятие"""

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        verbose_name="мероприятие",
        related_name="registrated_event"
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="участник",
        related_name="participants"
    )
    # notification = models.ForeignKey()
    registration_stage = models.CharField(
        "стадия регистрации",
        choices=RegistrationStageChoices.choices,
        default=RegistrationStageChoices.NOT_REGISTERED,
        max_length=MAX_LENGTH_REGISTRATION_STAGE
    )

    class Meta:
        verbose_name = "Регистрация"
        verbose_name_plural = "Регистрации"
