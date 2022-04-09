from rest_framework import serializers

from .models import LogFile


class LogFileSerializer(serializers.ModelSerializer):

    class Meta:
        model = LogFile
        fields = "__all__"



