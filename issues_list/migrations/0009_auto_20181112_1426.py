# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-12 14:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('issues_list', '0008_auto_20181108_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='votefor',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_votes', to='issues_list.Item'),
        ),
        migrations.AlterField(
            model_name='votefor',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_votes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='votefor',
            unique_together=set([('user', 'item')]),
        ),
    ]
