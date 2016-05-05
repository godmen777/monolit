# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 19:54
from __future__ import unicode_literals

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_post_preview_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='list_image_crop',
            field=image_cropping.fields.ImageRatioField('image', '750x365', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='\u041e\u0431\u0440\u0435\u0437\u043a\u0430 \u0434\u043b\u044f \u0441\u043f\u0438\u0441\u043a\u0430 \u0441\u0442\u0430\u0442\u0435\u0439 750x365'),
        ),
    ]