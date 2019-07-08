# coding: utf8
from django.urls import path

from apps.lines.api_v1 import endpoints

urlpatterns = ([

    path(
        route='lines/',
        view=endpoints.LineEndpoint.as_view(),
        name='v1_list_create_line'
    ),
    path(
        route='lines/<pk>/',
        view=endpoints.LineDetailEndpoint.as_view(),
        name='v1_retrieve_line'
    ),
    path(
        route='routes/',
        view=endpoints.RouteEndpoint.as_view(),
        name='v1_list_create_route'
    ),
    path(
        route='routes/<pk>/',
        view=endpoints.RouteDetailEndpoint.as_view(),
        name='v1_retrieve_route'
    ),

])
