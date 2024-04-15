from django.contrib import admin

from .models import (
    CustomUser,
    CustomUserFilter,
    CustomUserInfo,
    CustomUserSettings,
    NotificationEventType,
    NotificationMethod,
    NotificationTime,
    Specialization,
    SpecializationsInFilter,
)


class SpecializationFilterInline(admin.TabularInline):
    model = SpecializationsInFilter
    extra = 0


class CustomUserInfoInline(admin.TabularInline):
    model = CustomUserInfo
    extra = 0


class CustomUserSettingsInline(admin.TabularInline):
    model = CustomUserSettings
    extra = 0


class CustomUserFilterInline(admin.TabularInline):
    model = CustomUserFilter
    extra = 0


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """Управление пользователями"""

    list_display = (
        "id",
        "email",
        "first_name",
        "last_name",
        "phone",
        "role",
    )
    readonly_fields = ("created_at", "updated_at")
    list_display_links = ("id", "email")
    search_fields = ("email", "role")
    inlines = [
        CustomUserInfoInline,
        CustomUserSettingsInline,
        CustomUserFilterInline,
    ]


@admin.register(CustomUserInfo)
class CustomUserInfoAdmin(admin.ModelAdmin):
    """Управление доп. информацией"""

    list_display = (
        "user",
        "job",
        "experience",
        "specialization",
    )
    list_display_links = ("user",)
    search_fields = ("user",)
    empty_value_display = "-пусто-"


@admin.register(NotificationTime)
class NotificationTimeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(NotificationEventType)
class NotificationEventTypeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(NotificationMethod)
class NotificationMethodAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(CustomUserSettings)
class CustomUserSettingsAdmin(admin.ModelAdmin):
    """Управление настройками пользователя"""

    list_display = (
        "user",
        "ev_notification_start",
        "ev_notification_new",
    )
    list_display_links = ("user",)
    search_fields = ("user",)
    filter_horizontal = (
        "ev_notification_method",
        "ev_type_notification",
        "ev_notification_start_time",
    )
    empty_value_display = "-пусто-"


@admin.register(CustomUserFilter)
class CustomUserFilterAdmin(admin.ModelAdmin):
    """Управление фильтром пользователя"""

    list_display = (
        "user",
        "is_ev_online",
        "city",
    )
    list_display_links = ("user",)
    search_fields = ("user",)
    empty_value_display = "-пусто-"
    inlines = [SpecializationFilterInline]


@admin.register(Specialization)
class SpecializationAdmin(admin.ModelAdmin):
    """Управление направлениями"""

    list_display = ("pk", "name", "slug")
    list_display_links = ("name",)
    search_fields = ("name",)
    empty_value_display = "-пусто-"


@admin.register(SpecializationsInFilter)
class SpecializationsInFilterAdmin(admin.ModelAdmin):
    """Отображение направлений работы в фильтре пользователя."""

    list_display = ("filter", "get_user_name", "specialization")
    list_filter = ("filter", "specialization")
    list_display_links = ("get_user_name",)
    readonly_fields = ("get_user_name",)

    def get_user_name(self, obj):
        return obj.filter.user.email

    get_user_name.short_description = "Пользователь"
