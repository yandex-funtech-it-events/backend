from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.api.v1.events.serializers import ReportSerializer
from apps.api.v1.events.permissions import IsOrganizerOrReadOnly
from apps.events.models import Report


class ReportViewSet(viewsets.ModelViewSet):
    """Обработчик запросов на эндпойнты Report"""
    serializer_class = ReportSerializer
    permission_classes = (
        IsOrganizerOrReadOnly,
        IsAuthenticated
    )

    def get_queryset(self):
        queryset = Report.objects.filter(
            event=self.kwargs.get('event_id', None)
        )
        return queryset
