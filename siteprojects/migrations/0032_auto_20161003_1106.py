# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-03 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteprojects', '0031_projectimage_description_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='kubatura',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='\u041a\u0443\u0431\u0430\u0442\u0443\u0440\u0430'),
        ),
        migrations.AddField(
            model_name='project',
            name='living_area',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='\u0416\u0438\u043b\u0430\u044f \u043f\u043b\u043e\u0449\u0430\u0434\u044c'),
        ),
    ]
