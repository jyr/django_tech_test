# coding: utf8
from django.urls import reverse
from django.test import TestCase, tag

from rest_framework.test import APITestCase
from rest_framework import status

from apps.users.factories import (UserFactory, TokenFactory)
from apps.stations.factories import LocationFactory, StationFactory
from apps.stations.models import Location, Station

@tag('endpoints')
class LocationEndpointTest(APITestCase):

    url = reverse("api_v1_stations:v1_list_create_location")

    def setUp(self):
        """
        Initialize the objects to use in tests for Location endpoints.
        In stations app.
        """

        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_get_all_locations(self):
        """Test api can all locations."""

        LocationFactory(owner=self.user)

        response = self.client.get(self.url)
        response = response.json()

        self.assertEquals(response['body'].get('count'), 1)

    def test_post_a_location(self):
        """Test api can create a new location."""

        data = {
            "name": "Urbvan",
            "latitude": 19.388401,
            "longitude": -99.227358,
            "owner": self.user.id
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


@tag('endpoints')
class LocationDetailEndpointTest(APITestCase):

    def setUp(self):
        """
        Initialize the objects to use in tests for Location endpoints.
        In stations app.
        """

        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )
        self.location = LocationFactory(owner=self.user)

        self.url = reverse(
            "api_v1_stations:v1_retrieve_location",
            kwargs={'pk': self.location.id}
        )

    def test_get_a_location(self):
        """Test api get a location."""

        response = self.client.get(self.url, format='json')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.location)

    def test_put_a_location(self):
        """Test api can update a location."""

        data = {
            "name": "My new location",
            "latitude": "1.120000000000003",
            "longitude": "1.0000000000000004",
            "owner": self.user.id
        }

        response = self.client.put(self.url, data, format='json')

        new_name_location = response.data['body']['results'][0]['name']
        self.location.refresh_from_db()

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(new_name_location, 'My new location')
        self.assertEquals(self.location.name, new_name_location)

    def test_patch_a_location(self):
        """Test api can partial update a location."""

        data = {
            "latitude": "0.0000000000000300",
        }

        response = self.client.patch(self.url, data, format='json')
        new_latitude_location = '{0:f}'.format(
            response.data['body']['results'][0]['latitude']
        )
        self.location.refresh_from_db()


        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(new_latitude_location, '0.0000000000000300')
        self.assertEquals('{0:f}'.format(
            self.location.latitude),
            new_latitude_location
        )

    def test_delete_a_location(self):
        """Test api can delete a location."""

        LocationFactory(owner=self.user)

        locations = Location.objects.all()
        location_id = self.location.id
        response = self.client.delete(self.url, format='json')
        deleted_location = Location.objects.filter(id=location_id).exists()

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(len(locations) == 1)
        self.assertFalse(deleted_location)


@tag('endpoints')
class StationEndpointTest(APITestCase):
    url = reverse("api_v1_stations:v1_list_create_station")

    def setUp(self):
        """
        Initialize the objects to use in tests for Station endpoints.
        In stations app.
        """

        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)
        self.location = LocationFactory(owner=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_get_all_stations(self):
        """Test api can all stations."""

        for _ in range(3):
            StationFactory(owner=self.user, location=self.location)

        response = self.client.get(self.url)
        response = response.json()

        self.assertEquals(response['body'].get('count'), 3)

    def test_post_a_station(self):
        """Test api can create a new station."""

        data = {
            "location": self.location.id,
            "order": 12,
            "is_active": False,
            "owner": self.user.id
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)


@tag('endpoints')
class StationDetailEndpointTest(APITestCase):

    def setUp(self):
        """
        Initialize the objects to use in tests for Station endpoints.
        In stations app.
        """

        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )
        self.location = LocationFactory(owner=self.user)
        self.station = StationFactory(location=self.location, owner=self.user)

        self.url = reverse(
           "api_v1_stations:v1_retrieve_station",
           kwargs={'pk': self.station.id}
        )

    def test_get_a_station(self):
        """Test api get a station."""

        response = self.client.get(self.url, format='json')

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.station.id)

    def test_put_a_station(self):
        """Test api can update a station."""

        data = {
                "location": LocationFactory().id,
                "order": 12,
                "is_active": False,
                "owner": self.user.id
        }

        response = self.client.put(self.url, data, format='json')
        new_order_station = response.data['body']['results'][0]['order']
        self.station.refresh_from_db()

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(new_order_station, 12)
        self.assertEquals(self.station.order, new_order_station)

    def test_patch_a_station(self):
        """Test api can partial update a station."""

        data = {
            "is_active": False,
        }

        response = self.client.patch(self.url, data, format='json')
        new_state_station = response.data['body']['results'][0]['is_active']
        self.station.refresh_from_db()

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(new_state_station, False)
        self.assertEquals(self.station.is_active, new_state_station)

    def test_delete_a_station(self):
        """Test api can delete a station."""

        StationFactory(location=LocationFactory())

        stations = Station.objects.all()
        station_id = self.station.id
        response = self.client.delete(self.url, format='json')
        deleted_station = Station.objects.filter(id=station_id).exists()

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertTrue(len(stations) == 1)
        self.assertFalse(deleted_station)


@tag('endpoints')
class LineEndpointTest(APITestCase):
    pass


@tag('endpoints')
class LineDetailEndpointTest(APITestCase):
    pass


@tag('endpoints')
class RouteEndpointTest(APITestCase):
    pass


@tag('endpoints')
class RouteDetailEndpointTest(APITestCase):
    pass
