# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-25 17:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preingest', '0039_processstep_parent_step_pos'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='processstep',
            options={'ordering': ('parent_step_pos',)},
        ),
    ]
