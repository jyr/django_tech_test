from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.stations.models import Station, Location

@receiver(pre_save, sender=Location)
@receiver(pre_save, sender=Station)
def pre_save(sender, instance, *args, **kwargs):
    instance.id = create_id(instance.prefix)
