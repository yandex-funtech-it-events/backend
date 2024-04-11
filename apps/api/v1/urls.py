from django.urls import include, path
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    # path("", include("apps.api.v1.events.urls")),
    path("users/", include("apps.api.v1.users.urls")),
    # path('auth/', include('djoser.urls.jwt')),
    path("login/", TokenObtainPairView.as_view(), name="users_login"),
]
