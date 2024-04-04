from django.contrib import admin

from .models import Report


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("title", "speaker", "event",)
    list_filter = ("event", "speaker",)
    search_fields = ("title", "speaker",)
