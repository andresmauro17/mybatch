# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_empresa_ciudad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
