# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-04 14:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20160504_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
                ('template', models.CharField(help_text='\u043f\u0443\u0442\u044c \u0434\u043e \u0448\u0430\u0431\u043b\u043e\u043d\u0430, \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 "core/services_set.html"', max_length=200, verbose_name='\u0428\u0430\u0431\u043b\u043e\u043d')),
            ],
        ),
    ]
