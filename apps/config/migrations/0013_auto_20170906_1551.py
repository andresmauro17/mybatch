# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 20:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0012_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='certificado_calidad',
            field=models.FileField(blank=True, null=True, upload_to='pdf/config/material/certificado_calidad'),
        ),
        migrations.AlterField(
            model_name='material',
            name='ficha_tecnica',
            field=models.FileField(upload_to='pdf/config/material/ficha_tecnica'),
        ),
    ]