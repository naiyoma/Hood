# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 14:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('areahood', '0002_auto_20181019_1624'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='url',
            new_name='link',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='image_name',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='image_caption',
            new_name='post_description',
        ),
    ]
