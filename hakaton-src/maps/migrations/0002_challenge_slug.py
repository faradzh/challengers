# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-06 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='slug',
            field=models.SlugField(null=True, unique=True, verbose_name='Slug'),
        ),
    ]
