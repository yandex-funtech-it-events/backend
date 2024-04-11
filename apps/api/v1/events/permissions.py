from rest_framework import permissions

from apps.events.models import Report


class IsOrganizerOrReadOnly(permissions.BasePermission):
    """Проверка прав для организатора"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        if isinstance(obj, Report):
            return obj.event.creator == request.user
        return obj.creator == request.user


class IsModeratorOrReadOnly(permissions.BasePermission):
    """Проверка прав для модератора"""

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_moderator
