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
# Generated by Django 1.10 on 2016-08-24 12:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20160824_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_aip',
            field=models.ManyToManyField(through='profiles.ProfileAIPRel', to='profiles.ProfileAIP'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_classification',
            field=models.ManyToManyField(through='profiles.ProfileClassificationRel', to='profiles.ProfileClassification'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_content_type',
            field=models.ManyToManyField(through='profiles.ProfileContentTypeRel', to='profiles.ProfileContentType'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_data_selection',
            field=models.ManyToManyField(through='profiles.ProfileDataSelectionRel', to='profiles.ProfileDataSelection'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_dip',
            field=models.ManyToManyField(through='profiles.ProfileDIPRel', to='profiles.ProfileDIP'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_import',
            field=models.ManyToManyField(through='profiles.ProfileImportRel', to='profiles.ProfileImport'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_preservation_metadata',
            field=models.ManyToManyField(through='profiles.ProfilePreservationMetadataRel', to='profiles.ProfilePreservationMetadata'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_sip',
            field=models.ManyToManyField(through='profiles.ProfileSIPRel', to='profiles.ProfileSIP'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_submit_description',
            field=models.ManyToManyField(through='profiles.ProfileSubmitDescriptionRel', to='profiles.ProfileSubmitDescription'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_transfer_project',
            field=models.ManyToManyField(through='profiles.ProfileTransferProjectRel', to='profiles.ProfileTransferProject'),
        ),
        migrations.AddField(
            model_name='submissionagreement',
            name='profile_workflow',
            field=models.ManyToManyField(through='profiles.ProfileWorkflowRel', to='profiles.ProfileWorkflow'),
        ),
    ]
