# coding: utf8
from django.urls import path

from apps.stations.api_v1 import endpoints

urlpatterns = ([

    path(
        route='locations/',
        view=endpoints.LocationView.as_view(),
        name='v1_list_create_location'
    ),

])
