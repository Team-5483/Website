# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-04 17:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inventory', '0007_item_item_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_quantity',
            field=models.CharField(default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_unit_price',
            field=models.CharField(default='0', max_length=50),
        ),
    ]
