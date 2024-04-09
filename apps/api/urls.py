from rest_framework import routers

from .views import ReportViewSet


router_1 = routers.DefaultRouter()
router_1.register(
    # r'reports/<int:event_id>',
    r'reports/(?P<event_id>[^/.]+)',
    ReportViewSet,
    basename='reports/(?P<event_id>[^/.]+)'
)
