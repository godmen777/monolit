# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-03 10:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteprojects', '0030_remove_project_kubatura'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectimage',
            name='description_img',
            field=models.CharField(blank=True, max_length=100, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f'),
        ),
    ]
