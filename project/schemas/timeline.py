from rest_framework import serializers

from ..models import TimeLine


class TimeLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeLine
        fields = ["id", "title", "user", "project"]
