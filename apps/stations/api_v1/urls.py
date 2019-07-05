# coding: utf8
from django.urls import path

from apps.stations.api_v1 import endpoints

urlpatterns = ([

    path(
        route='locations/',
        view=endpoints.LocationEndpoint.as_view(),
        name='v1_list_create_location'
    ),
    path(
        route='locations/<pk>/',
        view=endpoints.LocationDetailEndpoint.as_view(),
        name='v1_retrieve_location'
    ),
    path(
        route='stations/',
        view=endpoints.StationEndpoint.as_view(),
        name='v1_list_create_station'
    ),
    path(
        route='stations/<pk>/',
        view=endpoints.StationDetailEndpoint.as_view(),
        name='v1_retrieve_station'
    ),

])
