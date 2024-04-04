from django.contrib import admin

from .models import Events, EventTags


@admin.register(EventTags)
class EventTagsAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "format", "creator", "moderator")
    list_filter = ("city", "format")
    search_fields = ("title", "description", "city")
    filter_horizontal = ("tags",)
