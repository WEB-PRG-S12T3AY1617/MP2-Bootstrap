# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-25 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=40)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('is_secondHand', models.BooleanField(default=False)),
                ('is_academic', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('is_Student', models.BooleanField(default=True)),
                ('degreeProgram', models.CharField(max_length=30, null=True)),
                ('office', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='tag',
            field=models.ManyToManyField(to='Marketplace.Tag'),
        ),
        migrations.AddField(
            model_name='item',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Marketplace.User'),
        ),
    ]
