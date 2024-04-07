from django.db import models

from apps.users.models import CustomUser
from apps.events.models import Events
from apps.core.constants import MAX_LENGTH_NOTIFICATION_TEXT


class Notification(models.Model):
    """Модель уведомления"""
    text = models.TextField(
        "текст уведомления",
        max_length=MAX_LENGTH_NOTIFICATION_TEXT
    )
    created_at = models.DateTimeField(
        "дата создания", auto_now_add=True,
    )
    date_popup = models.DateTimeField(
        "дата оповещения", default=None,
    )
    qrcode_ticket = models.ImageField(
        "qr код для мероприятия",
        blank=True, upload_to="qr_codes/"
    )
    event = models.ForeignKey(
        Events,
        on_delete=models.CASCADE,
        verbose_name="мероприятие",
        related_name="event_notification"
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name="участник",
        related_name="participant_notification"
    )

    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"

    def __str__(self) -> str:
        return self.text[:50]
