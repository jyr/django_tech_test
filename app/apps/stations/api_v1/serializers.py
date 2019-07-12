# coding: utf8
from rest_framework import serializers

from apps.stations.models import Location, Station


class LocationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Location
        fields = ('name', 'owner','latitude', 'longitude')

class StationSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    class Meta:
        model = Station
        fields = ('order', 'owner','is_active', 'location')
