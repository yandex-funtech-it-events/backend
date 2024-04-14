from django.urls import include, path

urlpatterns = [
    path("", include("apps.api.v1.events.urls")),
    path("", include("apps.api.v1.notifications.urls")),
    path("users/", include("apps.api.v1.users.urls")),
]
