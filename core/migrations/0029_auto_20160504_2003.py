# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 20:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0028_service_list_image_crop'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='list_image_crop',
            new_name='image_list_crop',
        ),
        migrations.RenameField(
            model_name='service',
            old_name='list_image_crop',
            new_name='image_list_crop',
        ),
    ]