# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Marketplace', '0009_auto_20170726_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Marketplace.Profile'),
        ),
    ]
