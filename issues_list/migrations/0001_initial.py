# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-05 18:09
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('content', models.TextField(max_length=200)),
                ('category', models.CharField(choices=[('Feature', 'Feature'), ('Bug', 'Bug')], default=False, max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('upvotes', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Ongoing', 'Ongoing'), ('Completed', 'Completed')], default=False, max_length=20)),
                ('assigned_to', models.CharField(choices=[('Not yet assigned', 'Not yet assigned'), ('Admin1', 'Admin1'), ('The Prof', 'The Prof'), ('Jane Doe', 'Jane Doe'), ('Jane Smith', 'Jane Smith'), ('John Doe', 'John Doe'), ('John Smith', 'John Smith')], default='Not yet Assigned', max_length=30)),
                ('completed_date', models.DateTimeField(auto_now=True, null=True)),
                ('progress', models.TextField(default='', help_text='Add progress comments to the status', max_length=200)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-upvotes'],
            },
        ),
    ]
