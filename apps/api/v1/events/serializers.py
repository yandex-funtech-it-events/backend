from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from django.shortcuts import get_object_or_404

from apps.events.models import Report, Events


class ReportSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Report"""

    event = serializers.PrimaryKeyRelatedField(read_only=True)
    speaker_photo = Base64ImageField()

    class Meta:
        model = Report
        fields = "__all__"

    def validate_event(self, value):

        if not Events.objects.filter(id=value).exists():
            raise serializers.ValidationError(
                f"Меропроиятие с id={value} не найдено"
            )
        return value

    def create(self, validated_data):
        event = get_object_or_404(
            Events,
            id=self.context.get("event_id")
        )
        report = Report.objects.create(
            event=event,
            **validated_data
        )
        return report
