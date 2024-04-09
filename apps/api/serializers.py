from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from apps.events.models import Report


class ReportSerializer(serializers.ModelSerializer):
    event = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    speaker_photo = Base64ImageField()

    class Meta:
        model = Report
        fields = "__all__"
