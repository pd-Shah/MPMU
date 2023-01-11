from django.contrib.auth.models import User
from django.db import models
from .common import CommonBaseModel


class Project(CommonBaseModel):
    users = models.ManyToManyField(User, through='TimeLine')
