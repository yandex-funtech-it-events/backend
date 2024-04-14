import datetime

from django.shortcuts import get_object_or_404
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from apps.events.models import Events
from apps.notifications.models import Notification

NOTIFICATION_TIME = datetime.time(10, 0)


class NotificationSerializer(serializers.ModelSerializer):
    """Сериализатор для уведомлений"""

    ticket_qr_code = Base64ImageField()

    class Meta:
        model = Notification
        fields = (
            "id",
            "text",
            "created_at",
            "notification_at",
            "ticket_qr_code",
        )

    def create(self, validated_data):
        event = get_object_or_404(Events, id=self.context.get("event_id"))
        user = self.context.get("request").user
        notification_at = datetime.datetime.combine(event.date_start, NOTIFICATION_TIME)

        notification = Notification.objects.create(
            event=event, user=user, notification_at=notification_at, **validated_data
        )
        return notification
