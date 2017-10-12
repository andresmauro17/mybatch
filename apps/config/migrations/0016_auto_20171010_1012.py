# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 15:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20171010_0841'),
        ('config', '0015_equipo_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='fabricante',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.Empresa'),
        ),
        migrations.AddField(
            model_name='material',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.Empresa'),
        ),
        migrations.AddField(
            model_name='producto',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.Empresa'),
        ),
        migrations.AddField(
            model_name='proveedor',
            name='empresa',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.Empresa'),
        ),
    ]
