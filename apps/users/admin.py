from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Управление пользователями"""

    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "role",
    )
    readonly_fields = ("created_at", "updated_at")
    list_display_links = ("id", "email")
    search_fields = ("email", "role")
