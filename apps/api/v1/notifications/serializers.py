import datetime
import qrcode
import os

from rest_framework import serializers
from django.shortcuts import get_object_or_404
from django.conf import settings
from drf_extra_fields.fields import Base64ImageField

from apps.notifications.models import Notification
from apps.events.models import Events


NOTIFICATION_TIME = datetime.time(10, 0)


def generate_qr(data_to_encode: str):
    qr_img = qrcode.make(data_to_encode)
    path = os.path.join(
        settings.MEDIA_ROOT,
        "qr_codes",
        f"{data_to_encode}.jpg"
    )
    qr_img.save(path)
    return f"{data_to_encode}.jpg"


class NotificationSerializer(serializers.ModelSerializer):
    """Сериализатор для уведомлений"""

    ticket_qr_code = Base64ImageField(required=False)

    class Meta:
        model = Notification
        fields = (
            "id",
            "text",
            "created_at",
            "notification_at",
            "ticket_qr_code",
        )
        extra_kwargs = {'ticket_qr_code': {'required': False}}

    def create(self, validated_data):
        event = get_object_or_404(
            Events,
            id=self.context.get("event_id")
        )
        user = self.context.get('request').user
        notification_at = datetime.datetime.combine(
            event.date_start,
            NOTIFICATION_TIME
        )
        print('creating_qr')
        qr_img_path = generate_qr(f'event_{event.id}_user_{user.id}')

        notification = Notification.objects.create(
            event=event,
            user=user,
            notification_at=notification_at,
            ticket_qr_code=qr_img_path,
            **validated_data
        )
        return notification
