from django.conf import settings
from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from log_aggregator.users.api.views import UserViewSet


if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)

urlpatterns = [
    path("", include("log_aggregator.aggregator.urls")),
]

app_name = "api"
urlpatterns += router.urls
