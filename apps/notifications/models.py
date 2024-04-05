from django.db import models

from apps.core.constants import MAX_LENGTH_NOTIFICATION_TEXT


# class Notification(models.Model):
#     """Модель уведомления"""
#     text = models.CharField(
#         "текст уведомления",
#         max_length=MAX_LENGTH_NOTIFICATION_TEXT
#     )
#     date_popup = models.DateTimeField(
#         "дата оповещения", blank=False, null=False
#     )
#     qrcode_ticket = models.ImageField(
#         "qr код для мероприятия",
#         blank=True, upload_to="qr_codes/"
#     )
