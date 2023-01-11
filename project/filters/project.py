from django_filters import FilterSet

from ..models import Project


class ProjectFilter(FilterSet):
    class Meta:
        model = Project
        fields = {
            'id': ['exact'],
            'title': ['icontains', 'exact'],
        }
