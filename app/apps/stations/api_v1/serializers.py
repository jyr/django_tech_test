# coding: utf8
from rest_framework import serializers

from apps.stations.models import Location, Station


class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        exclude = ('id', )

class StationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Station
        exclude = ('id', )
