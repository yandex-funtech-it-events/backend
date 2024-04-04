from django.contrib.auth.models import User
from django.db import models

from apps.core.constants import EventFieldLength
from apps.core.models import TimeStamp


class FormatChoices(models.TextChoices):
    """Формат проведения турнира"""

    ONLINE = ("online", "онлайн")
    OFFLINE = ("offline", "оффлайн")


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


class Events(TimeStamp):
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
        choices=FormatChoices.choices,
    )
    stream_link = models.URLField(
        "ссылка на трансляцию",
        max_length=EventFieldLength.MAX_LENGTH_STREAM_LINK.value,
        blank=True,
        default="",
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="организатор",
        related_name="events_created",
    )
    moderator = models.ForeignKey(
        User,
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
