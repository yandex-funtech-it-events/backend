from django.contrib import admin

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "event",
        "text",
        "created_at",
        "notification_at",
    )
    search_fields = (
        "user",
        "event",
    )
