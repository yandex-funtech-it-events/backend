from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.v1.events.views import ReportViewSet


router_events_v1 = DefaultRouter()
router_events_v1.register(
    r'reports/(?P<event_id>[^/.]+)',
    ReportViewSet,
    basename='reports/(?P<event_id>[^/.]+)'
)

urlpatterns = [path("", include(router_events_v1.urls))]
