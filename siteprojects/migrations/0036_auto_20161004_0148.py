# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-04 01:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteprojects', '0035_auto_20161003_1139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='kubatura',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='\u041a\u0443\u0431\u0430\u0442\u0443\u0440\u0430'),
            preserve_default=False,
        ),
    ]
