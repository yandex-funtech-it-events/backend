from django.contrib import admin

from .models import Report, Events


class ReportInline(admin.StackedInline):
    model = Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("title", "speaker", "event",)
    list_filter = ("event", "speaker",)
    search_fields = ("title", "speaker",)


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "format", "creator", "moderator")
    list_filter = ("city", "format")
    search_fields = ("title", "description", "city")
    filter_horizontal = ("tags",)
    inlines = [
        ReportInline,
    ]
