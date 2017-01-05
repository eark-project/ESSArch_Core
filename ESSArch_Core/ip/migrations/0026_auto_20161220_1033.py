# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-20 09:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0025_auto_20161216_1621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='informationpackage',
            options={'ordering': ['id'], 'permissions': (('set_uploaded', 'Can set IP as uploaded'), ('create_sip', 'Can create SIP'), ('submit_sip', 'Can submit SIP'), ('transfer_sip', 'Can transfer SIP'), ('change_sa', 'Can change SA connected to IP'), ('lock_sa', 'Can lock SA to IP'), ('unlock_profile', 'Can unlock profile connected to IP')), 'verbose_name': 'Information Package'},
        ),
    ]