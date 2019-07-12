# coding: utf8
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import Permission
from django.contrib.auth.models import User
from django.apps import apps

from guardian.core import ObjectPermissionChecker

from apps.utils import create_id, add_permissions

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
    name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey('auth.User', related_name='locations', on_delete=models.CASCADE)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.name

    @property
    def prefix(self):
        prefix = self.__class__.__name__.lower()[0:3] + '_'
        return prefix


class Station(models.Model):
    ## TODO: add docstring

    id = models.CharField(primary_key=True, max_length=30, unique=True)
    location = models.ForeignKey(
        'stations.Location',
        on_delete=models.DO_NOTHING,
        related_name='stations'
    )
    owner = models.ForeignKey('auth.User', related_name='stations', on_delete=models.CASCADE)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.id

    @property
    def prefix(self):
        prefix = self.__class__.__name__.lower()[0:3] + '_'
        return prefix

@receiver(pre_save, sender=Location)
@receiver(pre_save, sender=Station)
def stations_app_pre_save(sender, instance, *args, **kwargs):
    if not sender.objects.filter(pk=instance.id).exists():
        instance.id = create_id(instance.prefix)

@receiver(post_save, sender=Location)
@receiver(post_save, sender=Station)
def stations_app_post_save(sender, **kwargs):

    instance = kwargs['instance']
    model_name = instance._meta.model_name.capitalize()
    app_label = instance._meta.app_label
    model = apps.get_model(app_label, model_name)
    user = instance.owner
    object = model.objects.get(id=instance.id)

    add_permissions(user, object)
