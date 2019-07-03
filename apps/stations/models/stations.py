# coding: utf8
from django.db import models

from .locations import Location

from apps.utils import create_id


class Station(models.Model):

    id = models.CharField(default=create_id('sta_'), primary_key=True,
                          max_length=30, unique=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
