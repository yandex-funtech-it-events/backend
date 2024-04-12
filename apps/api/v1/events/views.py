from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from apps.api.v1.events.permissions import IsOrganizerOrReadOnly
from apps.api.v1.events.serializers import (
    EventsSerializer,
    EventTagsSerializer,
    FavoritesSerializers,
)
from apps.events.models import Events, EventTags, Favorites


class EventTagsViewSet(viewsets.ModelViewSet):
    """Обработчик запросов на эндпоинты EventTags"""

    queryset = EventTags.objects.all()
    serializer_class = EventTagsSerializer

    def get_permissions(self):
        if self.action in ["list", "create"]:
            return [IsAuthenticated()]
        elif self.action in ["partial_update", "destroy"]:
            return [IsOrganizerOrReadOnly()]
        else:
            return [AllowAny()]


class EventsViewSet(viewsets.ModelViewSet):
    """Обработчик запросов на эндпоинты Events"""

    queryset = Events.objects.all()
    serializer_class = EventsSerializer

    def get_permissions(self):
        if self.action in ["list", "create"]:
            return [IsAuthenticated()]
        elif self.action in ["partial_update", "destroy"]:
            return [IsOrganizerOrReadOnly()]
        else:
            return [AllowAny()]


class FavoritesViewSet(viewsets.ModelViewSet):
    """Обработчик запросов на эндпоинты Favorites"""

    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializers

    @action(detail=True, methods=["post"])
    def add_event_to_favorites(self, request, pk=None):
        event_id = request.data("event_id")
        favorite = self.get.object()
        favorite.events.add(event_id)
        favorite.save()
        return Response(
            {"message: Event added to favorites"}, status=status.HTTP_200_OK
        )

    @action(detail=True, methods=["delete"])
    def rm_event_from_favorites(self, request, pk=None):
        event_id = request.data("event_id")
        favorite = self.get.object()
        favorite.events.remove(event_id)
        favorite.save()
        return Response(
            {"message: Successfully removed from favorites"}, status=status.HTTP_200_OK
        )
