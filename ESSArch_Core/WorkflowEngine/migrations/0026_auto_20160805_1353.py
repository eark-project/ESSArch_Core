# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-05 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkflowEngine', '0025_remove_processstep_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processstep',
            name='type',
            field=models.IntegerField(choices=[(0, 'Receive new object'), (5, 'The object is ready to remodel'), (9, 'New object stable'), (10, "Object don't exist in AIS"), (11, "Object don't have any projectcode in AIS"), (12, "Object don't have any local policy"), (13, 'Object already have an AIP!'), (14, 'Object is not active!'), (19, 'Object got a policy'), (20, 'Object not updated from AIS'), (21, 'Object not accepted in AIS'), (24, 'Object accepted in AIS'), (25, 'SIP validate'), (30, 'Create AIP package'), (40, 'Create package checksum'), (50, 'AIP validate'), (60, 'Try to remove IngestObject'), (1000, 'Write AIP to longterm storage'), (1500, 'Remote AIP'), (2009, 'Remove temp AIP object OK'), (3000, 'Archived'), (5000, 'ControlArea'), (5100, 'WorkArea'), (9999, 'Deleted')], null=True),
        ),
    ]