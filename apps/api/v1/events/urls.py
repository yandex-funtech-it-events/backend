"""Настройка URL эндпоинтов Events API v1"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.api.v1.events.views import EventsViewSet, EventTagsViewSet, FavoritesViewSet

router_events_v1 = DefaultRouter()
router_events_v1.register("events", EventsViewSet, basename="events")
router_events_v1.register("tags", EventTagsViewSet, basename="tags")
router_events_v1.register("favorites", FavoritesViewSet, basename="favorites")

urlpatterns = [path("", include(router_events_v1.urls))]
