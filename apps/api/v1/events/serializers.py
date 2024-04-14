from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from django.shortcuts import get_object_or_404

from apps.events.models import (
    Events,
    EventTags,
    Report,
    Registration,
)


class EventTagsSerializer(serializers.ModelSerializer):
    """Сериализатор модели тэгов"""

    class Meta:
        model = EventTags
        fields = "__all__"


class EventsSerializer(serializers.ModelSerializer):
    """Сериализатор для работы с объектами events"""

    tags = EventTagsSerializer(many=True)

    class Meta:
        model = Events
        fields = (
            "id",
            "title",
            "description",
            "city",
            "format",
            "location",
            "creator",
            "moderator",
            "tags",
            "picture",
            "stream_link",
            "registration_open",
            "registration_close",
            "date_start",
            "date_end",
        )

    def update(self, instance, validated_data):
        for field in [
            "title",
            "description",
            "city",
            "format",
            "location",
            "creator",
            "moderator",
            "picture",
            "stream_link",
            "registration_open",
            "registration_close",
            "date_start",
            "date_end",
        ]:
            setattr(
                instance, field, validated_data.get(field, getattr(instance, field))
            )

        tags_data = validated_data.get("tags")
        if tags_data:
            instance.tags.clear()
            for tag_data in tags_data:
                tag, _ = EventTags.objects.get_or_create(**tag_data)
                instance.tags.add(tag)

        instance.save()
        return instance

    def create(self, validated_data):
        tags_data = validated_data.pop("tags")
        event = Events.objects.create(**validated_data)

        for tag_data in tags_data:
            tag, _ = EventTags.objects.get_or_create(**tag_data)
            event.tags.add(tag)
        return event


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


class RegistrationSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Registration"""
    event = serializers.PrimaryKeyRelatedField(
        read_only=True
    )
    user = serializers.PrimaryKeyRelatedField(
        read_only=True
    )

    class Meta:
        model = Registration
        fields = ("id", "event", "user", "created_at",)
