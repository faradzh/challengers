# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-06 15:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='upload/avatar_pic/', verbose_name='Profile image')),
                ('first_name', models.CharField(max_length=255, verbose_name='Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Surname')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='Birthday')),
                ('status', models.CharField(blank=True, max_length=255, null=True, verbose_name='Status')),
                ('phone', models.CharField(blank=True, max_length=30, null=True, verbose_name='Mobile phone')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Profile was created: ')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
