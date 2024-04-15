from django.urls import include, path
from rest_framework import routers

from apps.api.v1.users.views import (
    CustomUserFilterViewSet,
    CustomUserInfoViewSet,
    CustomUserSettingsViewSet,
    CustomUserViewSet,
)

router_users_v1 = routers.DefaultRouter()

router_users_v1.register("", CustomUserViewSet)
router_users_v1.register("filter", CustomUserFilterViewSet)
router_users_v1.register("info", CustomUserInfoViewSet)
router_users_v1.register("settings", CustomUserSettingsViewSet)


urlpatterns = [path("", include(router_users_v1.urls))]
