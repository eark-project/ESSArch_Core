# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-07 17:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0021_auto_20161107_1813'),
        ('ip', '0015_auto_20160915_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='informationpackage',
            name='SubmissionAgreementLocked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='informationpackage',
            name='profiles',
            field=models.ManyToManyField(related_name='information_packages', through='profiles.ProfileIP', to='profiles.Profile'),
        ),
    ]
