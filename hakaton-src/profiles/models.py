# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name=u'User')
    avatar = models.ImageField(u'Profile image', upload_to='upload/avatar_pic/', blank=True, null=True)
    first_name = models.CharField(u'Name', max_length=255)
    last_name = models.CharField(u'Surname', max_length=255)
    birthday = models.DateField(u'Birthday', blank=True, null=True)
    status = models.CharField(u'Status', max_length=255, blank=True, null=True)
    phone = models.CharField(u'Mobile phone', max_length=30, blank=True, null=True)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(u'Profile was created: ', auto_now_add=True)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def __str__(self):
        return self.first_name
