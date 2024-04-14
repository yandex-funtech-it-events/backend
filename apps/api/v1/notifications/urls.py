"""Настройка URL эндпоинтов Notification API v1"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.v1.notifications.views import (
    NotificationViewSet,
)

router_notification_v1 = DefaultRouter()
router_notification_v1.register(
    r'notifications/(?P<event_id>[^/.]+)',
    NotificationViewSet,
    basename='notifications/(?P<event_id>[^/.]+)'
)

urlpatterns = [path("", include(router_notification_v1.urls))]
