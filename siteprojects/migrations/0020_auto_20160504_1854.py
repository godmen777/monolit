# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 18:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteprojects', '0019_project_building_area'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ridge_height',
            field=models.IntegerField(default=5, verbose_name='\u0413\u0430\u0431\u0430\u0440\u0438\u0442\u044b \u0434\u043e\u043c\u0430'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='roof_area',
            field=models.IntegerField(default=5, verbose_name='\u041f\u043b\u043e\u0449\u0430\u0434\u044c \u043a\u0440\u044b\u0448\u0438'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='ugol_inclination',
            field=models.IntegerField(default=5, verbose_name='\u0423\u0433\u043e\u043b \u043d\u0430\u043a\u043b\u043e\u043d\u0430 \u043a\u0440\u044b\u0448\u0438'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='square',
            field=models.IntegerField(verbose_name='\u0412\u044b\u0441\u043e\u0442\u0430 \u0432 \u043a\u043e\u043d\u044c\u043a\u0435'),
        ),
    ]
