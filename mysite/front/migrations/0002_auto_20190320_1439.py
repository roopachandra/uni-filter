# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-20 14:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='description',
            field=models.TextField(default=''),
        ),
    ]