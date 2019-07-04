from django.contrib import admin
from apps.stations.models import Station, Location

admin.site.register(Station)
admin.site.register(Location)
