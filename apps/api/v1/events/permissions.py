from rest_framework import permissions

from apps.events.models import EventTags, Report
from apps.users.choice_classes import RoleChoices


class IsOrganizerOrReadOnly(permissions.BasePermission):
    """Проверка прав для организатора"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if isinstance(obj, Report):
            return obj.event.creator == request.user
        if isinstance(obj, EventTags):
            return request.user.role == RoleChoices.ORGANIZER
        return obj.creator == request.user


class IsModeratorOrReadOnly(permissions.BasePermission):
    """Проверка прав для модератора"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == RoleChoices.MODERATOR
