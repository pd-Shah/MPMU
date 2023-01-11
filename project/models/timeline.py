from django.db import models
from django.contrib.auth.models import User
from .common import CommonBaseModel


class TimeLine(CommonBaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
