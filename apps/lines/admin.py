from django.contrib import admin
from apps.lines.models import Line, Route

class LineAdmin(admin.ModelAdmin):
    exclude = ('id', )

class RouteAdmin(admin.ModelAdmin):
    exclude = ('id', )

admin.site.register(Line, LineAdmin)
admin.site.register(Route, RouteAdmin)
