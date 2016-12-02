from __future__ import unicode_literals
from django.utils import timezone
from django_google_maps import fields as map_fields
from django.db import models
from profiles.models import Profile


class Challenge(models.Model):
    address = map_fields.AddressField(max_length=200, verbose_name=u'Address')
    geolocation = map_fields.GeoLocationField(max_length=100, verbose_name=u'Geolocation')
    description = models.TextField(max_length=255, verbose_name=u'Description')
    reward_point = models.IntegerField(max_length=255, verbose_name=u'Reward Point')
    difficulty = models.IntegerField(max_length=200, verbose_name=u'Difficulty')
    photo = models.FileField(verbose_name=u'Photo')

    def __str__(self):
        return self.address


class Comment(models.Model):
    content = models.TextField(max_length=255, verbose_name=u'Content')
    date_created = models.DateField(default=timezone.now, verbose_name=u'Date created')
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class CompletedChallenge(models.Model):
    challenge = models.ForeignKey(Challenge)
    user = models.ForeignKey(Profile)


class AcceptedChallenge(models.Model):
    challenge = models.ForeignKey(Challenge)
    user = models.ForeignKey(Profile)

