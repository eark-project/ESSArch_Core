# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 11:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WorkflowEngine', '0037_auto_20160823_1220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='processstep',
            old_name='archiveobject',
            new_name='information_package',
        ),
    ]