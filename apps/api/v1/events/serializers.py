from rest_framework import serializers

from apps.events.models import Events, EventTags, Favorites


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


class FavoritesSerializers(serializers.ModelSerializer):
    """Сериализатор для работы с избранными мероприятиями"""

    class Meta:
        model = Favorites
        fields = "__all__"
