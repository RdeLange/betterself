# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 15:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('supplements', '0002_auto_20160524_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplementproduct',
            name='vendor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vendors.Vendor'),
        ),
    ]
