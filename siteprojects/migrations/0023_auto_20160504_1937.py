# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 19:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteprojects', '0022_project_combined_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='square',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='\u0412\u044b\u0441\u043e\u0442\u0430 \u0432 \u043a\u043e\u043d\u044c\u043a\u0435'),
        ),
    ]
