from django.db import models

from apps.core.constants import ReportFieldLength


class Report(models.Model):
    """Модель докладов мероприятия"""
    title = models.CharField(
        "название доклада",
        max_length=ReportFieldLength.MAX_LENGTH_TITLE.value,
        unique=True
    )
    description = models.CharField(
        "описание долкада",
        max_length=ReportFieldLength.MAX_LENGTH_DESCRIPTION.value,
        unique=True
    )
    date_start = models.DateField(
        "дата начала доклада", blank=True, null=True, db_index=True
    )
    date_end = models.DateField(
        "дата окончания доклада", blank=True, null=True, db_index=True
    )
    speaker = models.CharField(
        "Фамилиия и имя спикера",
        max_length=ReportFieldLength.MAX_LENGTH_SPEAKER.value,
    )
    speaker_title = models.CharField(
        "Должность спикера",
        max_length=ReportFieldLength.MAX_LENGTH_SPEAKER.value,
    )
    speaker_photo = models.ImageField(
        "Фотография спикера", blank=True, upload_to="speakers_pictures/"
    )
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        verbose_name="доклад",
        related_name="reported_at_event"
    )
