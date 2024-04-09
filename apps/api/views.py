from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import ReportSerializer
from apps.events.models import Report


class ReportViewSet(viewsets.ModelViewSet):
    serializer_class = ReportSerializer
    # Change later:
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = Report.objects.filter(
            event=self.kwargs.get('event_id', None)
        )
        return queryset
