from __future__ import unicode_literals
from django_google_maps import fields as map_fields
from django.db import models


class Challenge(models.Model):
    address = map_fields.AddressField(max_length=200)
    geolocation = map_fields.GeoLocationField(max_length=100)

    def __str__(self):
        return self.address