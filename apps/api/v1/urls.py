from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("", include("apps.api.v1.events.urls")),
    path("", include("apps.api.v1.notifications.urls")),
    path("users/", include("apps.api.v1.users.urls")),
    path("login/", TokenObtainPairView.as_view(), name="users_login"),
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger/",
        SpectacularSwaggerView.as_view(url_name="apps.api:schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/",
        SpectacularRedocView.as_view(url_name="apps.api:schema"),
        name="redoc",
    ),
]
