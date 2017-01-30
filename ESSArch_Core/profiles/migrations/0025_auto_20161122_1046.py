"""
    ESSArch is an open source archiving and digital preservation system

    ESSArch Core
    Copyright (C) 2005-2017 ES Solutions AB

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program. If not, see <http://www.gnu.org/licenses/>.

    Contact information:
    Web - http://www.essolutions.se
    Email - essarch@essolutions.se
"""

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0024_profileip_included'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submissionagreement',
            name='include_profile_classification',
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='include_profile_archival_description',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='include_profile_authority_information',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_type',
            field=models.CharField(choices=[(b'transfer_project', b'Transfer Project'), (b'content_type', b'Content Type'), (b'data_selection', b'Data Selection'), (b'authority_information', b'Authority Information'), (b'archival_description', b'Archival Description'), (b'import', b'Import'), (b'submit_description', b'Submit Description'), (b'sip', b'SIP'), (b'aip', b'AIP'), (b'dip', b'DIP'), (b'workflow', b'Workflow'), (b'preservation_metadata', b'Preservation Metadata'), (b'event', b'Event')], max_length=255),
        ),
    ]
