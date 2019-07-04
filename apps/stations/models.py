# coding: utf8
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models

from apps.utils import create_id

@receiver(pre_save)
def pre_save(sender, instance, *args, **kwargs):
    instance.id = create_id(instance.prefix)

class Location(models.Model):
    """ Location object is the representation of physical station

        Fields:
            id -- This is the unique identifier for object instance.
            name -- This is the common identifier for a physical location.
            coordinates --  Latitude and Longuitude as string.
                            example. "19.4094937,-99.1634261"
            geometry -- Similar to coordinate but using with postgis
    """

    id = models.CharField(primary_key=True, max_length=30, unique=True)
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)

    def __str__(self):
        return self.name

    @property
    def prefix(self):
        prefix = self.__class__.__name__.lower()[0:3] + '_'
        return prefix


class Station(models.Model):
    ## TODO: add docstring

    id = models.CharField(primary_key=True, max_length=30, unique=True)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.id + self.location.name

    @property
    def prefix(self):
        prefix = self.__class__.__name__.lower()[0:3] + '_'
        return prefix
