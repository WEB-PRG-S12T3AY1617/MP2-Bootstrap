# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Marketplace', '0002_remove_item_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='degreeProgram',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='office',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]