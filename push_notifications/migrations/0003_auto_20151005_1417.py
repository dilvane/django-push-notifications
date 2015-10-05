# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('push_notifications', '0002_auto_20151002_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='apnsdevice',
            name='language',
            field=models.CharField(max_length=255, default='en'),
        ),
        migrations.AddField(
            model_name='gcmdevice',
            name='language',
            field=models.CharField(max_length=255, default='en'),
        ),
    ]
