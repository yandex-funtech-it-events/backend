from django.contrib import admin

from .models import Registration


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "event",
        "registration_stage",
    )
    search_fields = ("user", "event")
