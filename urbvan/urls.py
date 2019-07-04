# coding: utf8
from django.contrib import admin
from django.urls import (include, path)

from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-token-auth/', views.obtain_auth_token),
    path('api/v1/', include(
        ('apps.stations.api_v1.urls', 'api_v1'),
        namespace='api_v1_stations')
	),
]
