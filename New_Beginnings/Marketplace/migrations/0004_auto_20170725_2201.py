# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marketplace', '0003_auto_20170725_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
