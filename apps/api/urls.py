from django.urls import include, path

app_name = "apps.api"

urlpatterns = [
    path("v1/", include("apps.api.v1.urls")),
]
