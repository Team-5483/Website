# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 22:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urmom', '0003_auto_20161019_1800'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='favorite',
            new_name='is_favorite',
        ),
    ]
