# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0008_auto_20170827_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='Proveedor',
            field=models.ManyToManyField(to='config.Proveedor'),
        ),
    ]