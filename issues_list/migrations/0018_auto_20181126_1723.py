# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-26 17:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('issues_list', '0017_auto_20181126_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='assigned_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='Enter as Y-m-d H:M:S (example 2018-11-10 11:30:00)', null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='completed_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='Enter as Y-m-d H:M:S (example 2018-11-10 11:30:00)', null=True),
        ),
    ]
