# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-08 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues_list', '0005_auto_20181106_2151'),
    ]

    operations = [
        migrations.AddField(
            model_name='votefor',
            name='voteup',
            field=models.BooleanField(default=False),
        ),
    ]
