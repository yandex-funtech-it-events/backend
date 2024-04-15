from djoser.serializers import UserCreateSerializer, UserSerializer
from drf_base64.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from apps.users.models import (
    CustomUser,
    CustomUserFilter,
    CustomUserInfo,
    CustomUserSettings,
    NotificationEventType,
    NotificationMethod,
    NotificationTime,
    Specialization,
)


class CustomUserCreateSerializer(UserCreateSerializer):
    """
    Сериализатор для создания нового пользователя.
    """

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "phone",
        )
        extra_kwargs = {
            "email": {"required": True},
            "password": {"write_only": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
            "phone": {"required": True},
        }


class SpecializationSerializer(serializers.ModelSerializer):
    """
    Сериализатор для чтения информации о направлении работы.
    """

    class Meta:
        model = Specialization
        fields = (
            "id",
            "name",
            "slug",
        )


class NotificationTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationTime
        fields = ("id", "name", "slug")


class NotificationMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationMethod
        fields = ("id", "name", "slug")


class NotificationEventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotificationEventType
        fields = ("id", "name", "slug")


class CustomUserInfoSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения доп. информации о пользователях.
    """

    specialization = SerializerMethodField()
    experience = serializers.CharField(source="get_experience_display", read_only=True)
    image = Base64ImageField()

    class Meta:
        model = CustomUserInfo
        fields = (
            "id",
            "image",
            "job",
            "experience",
            "specialization",
            "user_agree_personal_info",
            "user_agree_publish_cv",
            "user_agree_publish_media",
        )

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.save()
        return instance


class CustomUserSettingsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения настроек пользователя.
    """

    ev_notification_start_time = NotificationTimeSerializer(many=True, read_only=True)
    ev_type_notification_new = NotificationEventTypeSerializer(
        many=True, read_only=True
    )
    ev_notification_method = NotificationMethodSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUserSettings
        fields = (
            "ev_notification_start",
            "ev_notification_start_time",
            "ev_notification_new",
            "ev_type_notification_new",
            "ev_notification_method",
        )


class CustomUserFilterSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения фильтра пользователя.
    """

    specialization = SpecializationSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUserFilter
        fields = (
            "is_ev_online",
            "city",
            "specialization",
        )


class CustomUserSerializer(UserSerializer):
    """
    Сериализатор для чтения информации о пользователе.
    """

    info = CustomUserInfoSerializer()
    filter = CustomUserFilterSerializer()
    settings = CustomUserSettingsSerializer()

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "phone",
            "role",
            "info",
            "settings",
            "filter",
        )
