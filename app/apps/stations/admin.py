from django.contrib.auth.models import Permission
from django.contrib import admin

from apps.stations.models import Station, Location

from guardian.admin import GuardedModelAdmin

class LocationAdmin(GuardedModelAdmin):
    exclude = ('id', )


class StationAdmin(GuardedModelAdmin):
    exclude = ('id', )


admin.site.register(Station, StationAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Permission)
