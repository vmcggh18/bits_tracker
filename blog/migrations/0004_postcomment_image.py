# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-15 14:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20181211_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img'),
        ),
    ]