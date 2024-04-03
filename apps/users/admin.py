from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Управление пользователями"""
    list_display = (
        "id",
        "role",
        "username",
        "email",
        "first_name",
        "last_name"
    )
    list_display_links = ("id", "email")
    search_fields = ("email", "role")
