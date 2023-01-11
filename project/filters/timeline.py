from django_filters import FilterSet

from ..models import TimeLine


class TimeLineFilter(FilterSet):
    class Meta:
        model = TimeLine
        fields = {
            'id': ['exact'],
            'title': ['icontains', 'exact'],
        }
