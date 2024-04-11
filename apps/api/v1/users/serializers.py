from djoser.serializers import UserCreateSerializer, UserSerializer
from drf_base64.fields import Base64ImageField
from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from apps.users.models import (
    CustomUser,
    CustomUserFilter,
    CustomUserInfo,
    CustomUserSettings,
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
        )

    def get_specialization(self, obj):
        return obj.specialization.name if obj.specialization else None

    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.save()
        return instance


class CustomUserSettingsSerializer(serializers.ModelSerializer):
    """
    Сериализатор для получения настроек пользователя.
    """

    class Meta:
        model = CustomUserSettings
        fields = (
            "ev_notification_start",
            "ev_notification_new",
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

    info = SerializerMethodField()
    settings = SerializerMethodField()
    filter = SerializerMethodField()

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

    def get_info(self, obj):
        try:
            info = obj.info
            serializer = CustomUserInfoSerializer(info)
            return serializer.data
        except CustomUserInfo.DoesNotExist:
            return None

    def get_settings(self, obj):
        try:
            settings = obj.settings
            serializer = CustomUserSettingsSerializer(settings)
            return serializer.data
        except CustomUserSettings.DoesNotExist:
            return None

    def get_filter(self, obj):
        filter = {}
        try:
            filter["is_ev_online"] = obj.filter.is_ev_online
            filter["city"] = obj.filter.city
            filter["specializations"] = [
                spec.name for spec in obj.filter.specialization.all()
            ]
        except CustomUserFilter.DoesNotExist:
            return None
        return filter
