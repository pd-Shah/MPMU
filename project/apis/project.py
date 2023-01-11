from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..filters import ProjectFilter
from ..models import Project
from ..permissions import IsOwner, CanCreate
from ..schemas import ProjectSerializer


class ViewSetProject(
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet, ):
    filter_class = ProjectFilter
    permission_classes = (IsAuthenticated, CanCreate, IsOwner)

    def get_queryset(self):
        return Project.objects.prefetch_related('timeline_set', 'users').filter(users__in=(self.request.user, ))

    def get_serializer_class(self):
        return ProjectSerializer