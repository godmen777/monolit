# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 19:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_service_recent_posts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='recent_posts',
        ),
        migrations.AddField(
            model_name='page',
            name='service',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.Service', verbose_name='\u0421\u0432\u044f\u0437\u0430\u0442\u044c \u0441 \u0443\u0441\u043b\u0443\u0433\u043e\u0439'),
            preserve_default=False,
        ),
    ]
