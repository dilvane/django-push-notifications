# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import push_notifications.fields


class Migration(migrations.Migration):

    dependencies = [
        ('push_notifications', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apnsdevice',
            name='device_id',
            field=models.UUIDField(verbose_name='Device ID', blank=True, null=True, db_index=True, help_text='UDID / UIDevice.identifierForVendor()'),
        ),
        migrations.AlterField(
            model_name='gcmdevice',
            name='device_id',
            field=push_notifications.fields.HexIntegerField(verbose_name='Device ID', help_text='ANDROID_ID / TelephonyManager.getDeviceId() (always as hex)', blank=True, null=True, db_index=True),
        ),
    ]
