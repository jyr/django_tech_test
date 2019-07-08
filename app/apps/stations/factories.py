# coding: utf8
import factory

from .models import Location, Station


class LocationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Location

    name = factory.Faker('slug')
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')


class StationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Station

    id = 'sta_20197633059d4231eab'
    location = LocationFactory()
    order = factory.Faker('random_number')
    is_active = factory.Faker('boolean')
