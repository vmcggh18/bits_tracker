# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-03 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issues_list', '0006_auto_20181103_1945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='author',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='item',
            name='assigned_to',
            field=models.CharField(choices=[('Not yet assigned', 'Not yet assigned'), ('Admin1', 'Admin1'), ('The Prof', 'The Prof'), ('Jane Doe', 'Jane Doe'), ('Jane Smith', 'Jane Smith'), ('John Doe', 'John Doe'), ('John Smith', 'John Smith')], default='Not yet Assigned', max_length=30),
        ),
    ]
