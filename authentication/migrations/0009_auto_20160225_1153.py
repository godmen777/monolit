# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-25 11:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_auto_20160225_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
