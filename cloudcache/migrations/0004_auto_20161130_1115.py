# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-11-30 18:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cloudcache', '0003_auto_20160426_1451'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notebook',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='notebook',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='checklist',
            name='notebook',
        ),
        migrations.RemoveField(
            model_name='note',
            name='notebook',
        ),
        migrations.AddField(
            model_name='checklist',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='lists', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='note',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Notebook',
        ),
    ]