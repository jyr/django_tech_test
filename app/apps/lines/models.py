# coding: utf8
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.stations.models import Station

from apps.utils import create_id


class Line(models.Model):

    id = models.CharField(default=create_id('line_'), primary_key=True,
                          max_length=30, unique=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=8)

    def __str__(self):
        return self.name

    @property
    def prefix(self):
        prefix = self.__class__.__name__.lower()[0:3] + '_'
        return prefix


class Route(models.Model):

    id = models.CharField(default=create_id('route_'), primary_key=True,
                          max_length=30, unique=True)
    line = models.ForeignKey(Line, on_delete=models.DO_NOTHING)
    stations = models.ManyToManyField(Station)
    direction = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.line.name

    @property
    def prefix(self):
        prefix = self.__class__.__name__.lower()[0:3] + '_'
        return prefix

@receiver(pre_save, sender=Line)
@receiver(pre_save, sender=Route)
def pre_save(sender, instance, *args, **kwargs):
    if not sender.objects.filter(pk=instance.id).exists():
        instance.id = create_id(instance.prefix)
