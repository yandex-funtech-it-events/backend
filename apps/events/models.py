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
    date_start = models.DateTimeField(
        "дата начала доклада", blank=True, null=True
    )
    date_end = models.DateTimeField(
        "дата окончания доклада", blank=True, null=True
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
        Event,
        on_delete=models.CASCADE,
        verbose_name="доклад",
        related_name="reported_at_event"
    )

    class Meta:
        verbose_name = 'Доклад'
        verbose_name_plural = "Доклады"
        ordering = ["-date_start"]

    def __str__(self):
        return str(self.title[:50])
