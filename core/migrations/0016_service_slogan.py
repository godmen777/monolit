# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 13:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_auto_20160420_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='slogan',
            field=models.CharField(default='', max_length=200, verbose_name='\u0421\u043b\u043e\u0433\u0430\u043d'),
            preserve_default=False,
        ),
    ]
