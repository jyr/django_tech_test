# coding: utf8
from rest_framework import serializers

from apps.stations.models import Location


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        exclude = ('id', )
