from rest_framework import viewsets

from apps.api.v1.notifications.serializers import (
    NotificationSerializer,
)
from apps.notifications.models import Notification


class NotificationViewSet(viewsets.ModelViewSet):
    """Обработчик запросов на эндпойнты Notification"""

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["event_id"] = self.kwargs.get("event_id", None)
        return context

    def get_queryset(self):
        queryset = Notification.objects.filter(
            event=self.kwargs.get("event_id", None)
        )
        return queryset
