# coding: utf8
from django.urls import reverse

from rest_framework.test import APITestCase
from rest_framework import status

from apps.users.factories import (UserFactory, TokenFactory)
from apps.stations.factories import LocationFactory
from apps.stations.models import Location


class LocationEndpointTest(APITestCase):

    url = reverse("api_v1_stations:v1_list_create_location")

    def setUp(self):
        """Initialize the objects to use."""

        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )

    def test_get_all_locations(self):
        """Test api can all locations."""

        LocationFactory()

        response = self.client.get(self.url)
        response = response.json()

        self.assertEquals(response['body'].get('count'), 1)

    def test_post_a_location(self):
        """Test api can create a new location."""

        data = {
            "name": "Urbvan",
            "latitude": 19.388401,
            "longitude": -99.227358
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

class LocationDetailEndpointTest(APITestCase):

    def setUp(self):
        """Initialize the objects to use."""

        self.user = UserFactory()
        self.user_token = TokenFactory(user=self.user)

        self.client.credentials(
            HTTP_AUTHORIZATION="Urbvan {}".format(self.user_token.key)
        )
        self.location = LocationFactory()

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
            "longitude": "1.0000000000000004"
        }

        response = self.client.put(self.url, data, format='json')
        new_name_location = response.data['body']['results'][0]['name']

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(new_name_location, 'My new location')

    def test_patch_a_location(self):
        """Test api can partial update a location."""

        data = {
            "latitude": "0.0000000000000300",
        }

        response = self.client.patch(self.url, data, format='json')
        new_name_location = '{0:f}'.format(response.data['body']['results'][0]['latitude'])


        self.assertEquals(response.status_code, status.HTTP_200_OK)
        self.assertEquals(new_name_location, '0.0000000000000300')

    def test_delete_alocation(self):
        """Test api can delete a location."""

        location_id = self.location.id
        response = self.client.delete(self.url, format='json')
        exists = Location.objects.filter(id=location_id).exists()

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEquals(exists, False)
