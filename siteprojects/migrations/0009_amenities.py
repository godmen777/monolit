# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-10 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteprojects', '0008_auto_20160410_1208'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0435\u043a\u0442\u0430')),
                ('checked', models.BooleanField(default=False)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteprojects.Project')),
            ],
            options={
                'verbose_name': '\u0423\u0434\u043e\u0431\u0441\u0442\u0432\u043e',
                'verbose_name_plural': '\u0423\u0434\u043e\u0431\u0441\u0442\u0432\u0430',
            },
        ),
    ]
