from djoser.views import UserViewSet
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from apps.api.v1.users.permissions import IsOwnerOrAdminOrReadOnly
from apps.api.v1.users.serializers import (
    CustomUserCreateSerializer,
    CustomUserFilterSerializer,
    CustomUserInfoSerializer,
    CustomUserSerializer,
    CustomUserSettingsSerializer,
    NotificationEventTypeSerializer,
    NotificationMethodSerializer,
    NotificationTimeSerializer,
)
from apps.users.models import (
    CustomUser,
    CustomUserFilter,
    CustomUserInfo,
    CustomUserSettings,
    NotificationEventType,
    NotificationMethod,
    NotificationTime,
)


class NotificationTimeViewSet(ReadOnlyModelViewSet):
    """
    Представление для получения времени уведомления.
    """

    queryset = NotificationTime.objects.all()
    serializer_class = NotificationTimeSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly,)


class NotificationEventTypeViewSet(ReadOnlyModelViewSet):
    """
    Представление для получения типа мероприятия для уведомления.
    """

    queryset = NotificationEventType.objects.all()
    serializer_class = NotificationEventTypeSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly,)


class NotificationMethodViewSet(ReadOnlyModelViewSet):
    """
    Представление для получения способа уведомления.
    """

    queryset = NotificationMethod.objects.all()
    serializer_class = NotificationMethodSerializer
    permission_classes = (IsOwnerOrAdminOrReadOnly,)


class CustomUserViewSet(UserViewSet):
    """
    Представление для получения информации о пользователях.
    """

    queryset = CustomUser.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        """
        Выбор сериализатора в зависимости от
        просмотра или создания пользователя.
        """
        if self.request.method in SAFE_METHODS:
            return CustomUserSerializer
        return CustomUserCreateSerializer


class CustomUserInfoViewSet(ModelViewSet):
    """
    Представление для получения доп. информации о пользователях.
    """

    queryset = CustomUserInfo.objects.all()
    serializer_class = CustomUserInfoSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]


class CustomUserSettingsViewSet(ModelViewSet):
    """
    Представление для получения настроек пользователя.
    """

    queryset = CustomUserSettings.objects.all()
    serializer_class = CustomUserSettingsSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return CustomUserSettings.objects.all()
        else:
            return CustomUserSettings.objects.filter(user=user)


class CustomUserFilterViewSet(ModelViewSet):
    """
    Представление для получения фильтра пользователя.
    """

    queryset = CustomUserFilter.objects.all()
    serializer_class = CustomUserFilterSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return CustomUserFilter.objects.all()
        else:
            return CustomUserFilter.objects.filter(user=user)
