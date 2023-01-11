from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..filters import ProjectFilter
from ..models import Project
from ..permissions import CanCreate
from ..schemas import ProjectSerializer


class ViewSetProject(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet, ):
    filter_class = ProjectFilter
    permission_classes = (IsAuthenticated, CanCreate)

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
        return ProjectSerializer
