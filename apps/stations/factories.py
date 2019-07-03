# coding: utf8
import factory

from .models import Location


class LocationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Location

    name = factory.Faker('slug')
    latitude = factory.Faker('latitude')
    longitude = factory.Faker('longitude')
