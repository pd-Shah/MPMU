from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..filters import TimeLineFilter
from ..models import TimeLine
from ..permissions import CanCreate, IsOwner
from ..schemas import TimeLineSerializer


class ViewSetTimeLine(
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet, ):
    filter_class = TimeLineFilter
    permission_classes = (IsAuthenticated, CanCreate, IsOwner)

    def get_queryset(self):
        return TimeLine.objects.select_related('project', 'user').filter(user=self.request.user)
        
    def get_serializer_class(self):
        return TimeLineSerializer