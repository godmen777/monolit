# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-10 14:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_auto_20160227_2303'),
    ]

    operations = [
        migrations.AddField(
            model_name='performerprofile',
            name='about',
            field=models.CharField(default='\u0412\u0430\u0448\u0435 \u0434\u043e\u0432\u0435\u0440\u0438\u0435 - \u044d\u0442\u043e \u0442\u043e \u0447\u0435\u043c \u043c\u044b \u0434\u0435\u0439\u0441\u0442\u0432\u0438\u0442\u0435\u043b\u044c\u043d\u043e \u0434\u043e\u0440\u043e\u0436\u0438\u043c', max_length=200, verbose_name='\u041a\u0440\u0430\u0442\u043a\u043e \u043e \u0441\u0435\u0431\u0435'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='performerprofile',
            name='od',
            field=models.CharField(blank=True, max_length=200, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u043e\u0434\u043d\u043e\u043a\u043b\u0430\u0441\u0441\u043d\u0438\u043a\u0438'),
        ),
        migrations.AddField(
            model_name='performerprofile',
            name='skype',
            field=models.CharField(blank=True, max_length=200, verbose_name='\u043b\u043e\u0433\u0438\u043d \u0441\u043a\u0430\u0439\u043f'),
        ),
        migrations.AddField(
            model_name='performerprofile',
            name='vk',
            field=models.CharField(blank=True, max_length=200, verbose_name='\u0441\u0441\u044b\u043b\u043a\u0430 \u0432\u043a\u043e\u043d\u0442\u0430\u043a\u0442\u0435'),
        ),
        migrations.AlterField(
            model_name='performerprofile',
            name='first_name',
            field=models.CharField(blank=True, max_length=40, verbose_name='\u0418\u043c\u044f'),
        ),
        migrations.AlterField(
            model_name='performerprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=40, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f'),
        ),
    ]