from django.test import TestCase, tag

from apps.stations.models import Location, Station
from apps.stations.api_v1.serializers import LocationSerializer

@tag('serializers')
class LocationSerializerTest(TestCase):
    """Test for location serializer"""

    def setUp(self):
        self.location_attributes = {
            "name": "My new location",
            "latitude": "1.120000000000003",
            "longitude": "1.0000000000000004"
        }

        self.serializer_data = {
            "name": "My new location",
            "latitude": "1.120000000000003",
            "longitude": "1.0000000000000004"
        }


        self.location = Location.objects.create(**self.location_attributes)
        self.serializer = LocationSerializer(instance=self.location)

    def test_contains_expected_fields(self):
        """Checks if serializer data contains model's expected fields"""

        data = self.serializer.data

        self.assertCountEqual(
            data.keys(), [
                "name",
                "latitude",
                "longitude"
            ])
