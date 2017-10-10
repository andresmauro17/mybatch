# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 18:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_auto_20170811_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fabricante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_fabricante', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre_proveedor', models.CharField(max_length=150)),
            ],
        ),
        migrations.AlterField(
            model_name='equipo',
            name='marca',
            field=models.CharField(default='no aplica', max_length=50),
        ),
    ]