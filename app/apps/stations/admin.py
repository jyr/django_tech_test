from django.contrib import admin
from apps.stations.models import Station, Location

class LocationAdmin(admin.ModelAdmin):
    exclude = ('id', )

class StationAdmin(admin.ModelAdmin):
    exclude = ('id', )

admin.site.register(Station, StationAdmin)
admin.site.register(Location, LocationAdmin)
