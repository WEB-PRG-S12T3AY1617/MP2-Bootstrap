# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 06:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marketplace', '0010_item_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='displayPic',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
