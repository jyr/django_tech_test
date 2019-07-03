# coding: utf8
from django.db import models

from apps.stations.models import Station

from apps.utils import create_id


class Line(models.Model):

    id = models.CharField(default=create_id('line_'), primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)


class Route(models.Model):

    id = models.CharField(default=create_id('route_'), primary_key=True,
                          max_length=30, unique=True)
    line = models.ForeignKey(Line, on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(Station)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
