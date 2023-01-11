from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..filters import TimeLineFilter
from ..models import TimeLine
from ..permissions import CanCreate
from ..schemas import TimeLineSerializer


class ViewSetTimeLine(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet, ):
    filter_class = TimeLineFilter
    permission_classes = (IsAuthenticated, CanCreate)

    def get_queryset(self):
        return TimeLine.objects.all()

    def get_serializer_class(self):
        return TimeLineSerializer
