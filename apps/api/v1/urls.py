from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("", include("apps.api.v1.events.urls")),
    path("", include("apps.api.v1.notifications.urls")),
    path("users/", include("apps.api.v1.users.urls")),
    path("login/", TokenObtainPairView.as_view(), name="users_login"),
]
