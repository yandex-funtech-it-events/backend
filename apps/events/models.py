from django.db import models

from apps.core.constants import (
    MAX_LENGTH_REGISTRATION_STAGE,
    EventFieldLength,
    ReportFieldLength,
)
from apps.core.models import EventTimeStamp
from apps.events import choice_classes
from apps.users.models import CustomUser


class EventTags(models.Model):
    """Модель тегов мероприятия"""

    name = models.CharField(
        """тег мероприятия""",
        max_length=EventFieldLength.MAX_LENGTH_TAG.value,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = "тег"
        verbose_name_plural = "теги"

    def __str__(self):
        return self.name


class Events(EventTimeStamp):
    """Модель мероприятий"""

    title = models.CharField(
        "название", max_length=EventFieldLength.MAX_LENGTH_TITLE.value, unique=True
    )
    description = models.TextField(
        "описание", max_length=EventFieldLength.MAX_LENGTH_DESCRIPTION.value
    )
    city = models.CharField(
        "город мероприятия",
        max_length=EventFieldLength.MAX_LENGTH_CITY.value,
        blank=True,
        db_index=True,
    )
    picture = models.ImageField(
        "обложка мероприятия", blank=True, upload_to="events_pictures/"
    )
    location = models.CharField(
        "адрес мероприятия",
        max_length=EventFieldLength.MAX_LENGTH_LOCATION.value,
        blank=True,
    )
    format = models.CharField(
        "формат мероприятия",
        max_length=EventFieldLength.MAX_LENGTH_FORMAT.value,
        choices=choice_classes.FormatChoices.choices,
    )
    stream_link = models.URLField(
        "ссылка на трансляцию",
        max_length=EventFieldLength.MAX_LENGTH_STREAM_LINK.value,
        blank=True,
        default="",
    )
    creator = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="организатор",
        related_name="events_created",
    )
    moderator = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="модератор",
        related_name="events_moderated",
    )
    tags = models.ManyToManyField(EventTags, verbose_name="тег")

    class Meta:
        verbose_name = "мероприятие"
        verbose_name_plural = "мероприятия"
        ordering = ("id", "created_at", "creator")

    def __str__(self):
        return self.title


class Report(models.Model):
    """Модель докладов мероприятия"""

    title = models.CharField(
        "название доклада",
        max_length=ReportFieldLength.MAX_LENGTH_TITLE.value,
        unique=True,
    )
    description = models.TextField(
        "описание долкада",
        max_length=ReportFieldLength.MAX_LENGTH_DESCRIPTION.value,
        unique=True,
    )
    date_start = models.DateTimeField(
        "дата начала доклада", default=None, db_index=True
    )
    date_end = models.DateTimeField(
        "дата окончания доклада", default=None, db_index=True
    )
    speaker = models.CharField(
        "Фамилиия и имя спикера",
        max_length=ReportFieldLength.MAX_LENGTH_SPEAKER.value,
    )
    speaker_title = models.CharField(
        "Должность спикера",
        max_length=ReportFieldLength.MAX_LENGTH_SPEAKER_TITLE.value,
    )
    speaker_photo = models.ImageField(
        "Фотография спикера", blank=True, upload_to="speakers_pictures/"
    )
    event = models.ForeignKey(
        Events,
        on_delete=models.CASCADE,
        verbose_name="доклад",
        related_name="reported_at_event",
    )

    class Meta:
        verbose_name = "Доклад"
        verbose_name_plural = "Доклады"
        ordering = ["-date_start"]

    def __str__(self):
        return str(self.title[:50])


class Registration(models.Model):
    """Модель регистрации на мероприятие"""

    event = models.ForeignKey(
        Events,
        on_delete=models.CASCADE,
        verbose_name="мероприятие",
        related_name="registrated_event",
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="участник",
        related_name="participants",
    )
    # notification = models.ForeignKey(
    #     Notification,
    #     on_delete=models.SET_NULL,
    #     verbose_name="уведомление",
    #     related_name="notifications"
    # )
    registration_stage = models.CharField(
        "стадия регистрации",
        choices=choice_classes.RegistrationStageChoices.choices,
        default=choice_classes.RegistrationStageChoices.NOT_REGISTERED,
        max_length=MAX_LENGTH_REGISTRATION_STAGE,
    )

    class Meta:
        verbose_name = "Регистрация"
        verbose_name_plural = "Регистрации"
