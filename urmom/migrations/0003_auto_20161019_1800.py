# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-19 22:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('urmom', '0002_song_is_favorite'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='is_favorite',
            new_name='favorite',
        ),
    ]