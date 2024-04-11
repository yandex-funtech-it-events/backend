from django.urls import include, path
from rest_framework import routers

from apps.api.v1.users.views import CustomUserViewSet, SpecializationViewSet

router_users_v1 = routers.DefaultRouter()

router_users_v1.register("", CustomUserViewSet)
router_users_v1.register("specialization_id", SpecializationViewSet)


urlpatterns = [path("", include(router_users_v1.urls))]
