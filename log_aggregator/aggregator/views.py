from django.db.models import Q
from rest_framework import generics, permissions
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes

from .serializers import LogFileSerializer
from .models import LogFile
from .pagination import CustomLimitOffsetPagination


class LogFileListView(generics.ListAPIView):
    pagination_class = CustomLimitOffsetPagination
    serializer_class = LogFileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = LogFile.objects
        ip_address = self.request.query_params.get("ip_address")
        high_date = self.request.query_params.get("high_date")
        low_date = self.request.query_params.get("low_date")
        if ip_address:
            queryset = queryset.filter(ip_address=ip_address)
            return queryset
        if high_date:
            queryset = queryset.filter(timestamp__lte=high_date)
            return queryset
        if low_date:
            queryset = queryset.filter(timestamp__gte=low_date)
            return queryset
        if high_date and low_date:
            queryset = queryset.filter(timestamp__range=(low_date, high_date))
            return queryset
        if high_date and low_date and ip_address:
            queryset = queryset.filter(
                Q(timestamp__range=(low_date, high_date)) |
                Q(ip_address=ip_address)
            )
            return queryset
        return queryset.all()

    @extend_schema(
        parameters=[
            OpenApiParameter(
                "low_date",
                OpenApiTypes.DATETIME,
                description="Минимальная дата лога(От)"
            ),
            OpenApiParameter(
                "high_date",
                OpenApiTypes.DATETIME,
                description="Максимальная дата лога(До)"
            ),
        ],
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


