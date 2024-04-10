from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from apps.api.v1.events.permissions import IsOrganizerOrReadOnly
from apps.api.v1.events.serializers import EventsSerializer, EventTagsSerializer
from apps.events.models import Events, EventTags


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
        if self.action == "list":
            return [IsAuthenticated()]
        elif self.action == "create":
            return [IsAuthenticated()]
        elif self.action in ["partial_update", "destroy"]:
            return [IsOrganizerOrReadOnly()]
        else:
            return [AllowAny()]
