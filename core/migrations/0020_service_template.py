# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Template', verbose_name='\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0448\u0430\u0431\u043b\u043e\u043d'),
        ),
    ]
