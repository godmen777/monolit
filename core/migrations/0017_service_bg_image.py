# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_service_slogan'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='bg_image',
            field=models.ImageField(default='', upload_to='services', verbose_name='\u0424\u043e\u043d\u043e\u0432\u043e\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
            preserve_default=False,
        ),
    ]
