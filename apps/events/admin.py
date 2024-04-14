from django.contrib import admin

from .models import Events, EventTags, Favorites, Registration, Report


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "event",
        "registration_stage",
    )
    search_fields = ("user", "event")


class ReportInline(admin.StackedInline):
    model = Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = (
        "topic",
        "speaker",
        "event",
    )
    list_filter = (
        "event",
        "speaker",
    )
    search_fields = (
        "topic",
        "speaker",
    )


@admin.register(EventTags)
class EventTagsAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "city", "format", "creator", "moderator")
    list_filter = ("city", "format")
    search_fields = ("title", "description", "city")
    filter_horizontal = ("tags",)
    inlines = [
        ReportInline,
    ]


@admin.register(Favorites)
class FavoritesAdmin(admin.ModelAdmin):
    list_display = ["user", "event"]
    list_filter = ["user"]
