# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-22 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkflowEngine', '0010_processtask_undo_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='processtask',
            name='retried',
            field=models.BooleanField(default=False),
        ),
    ]