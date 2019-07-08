from django.test import TestCase, tag

from apps.stations.models import Location, Station


@tag('models')
class LocationTest(TestCase):
    """
    This tests are written to check the functionality of
    the methods of the Location Model
    """

    def setUp(self):
        self.default_data = {
            "name": "My new location",
            "latitude": "1.120000000000003",
            "longitude": "1.0000000000000004"
        }

    def test_generate_prefix_correctly(self):
        """
        Ensures that prefix is correctly generated for creating the instance's
        id
        """

        location = Location.objects.create(**self.default_data)
        prefix = 'loc_'
        instance_id = location.id

        self.assertTrue(prefix in instance_id)
