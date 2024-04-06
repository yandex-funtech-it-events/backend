from django.contrib import admin

from .models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "event",
        "text",
        "created_at",
        "date_popup"
    )
    search_fields = ("user", "event")
