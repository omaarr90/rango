# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-02 19:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_page_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2016, 9, 2, 19, 1, 4, 17725, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
