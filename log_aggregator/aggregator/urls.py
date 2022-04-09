from django.urls import path

from .views import LogFileListView


urlpatterns = [
    path("logs/", LogFileListView.as_view(), name="logs"),
]
