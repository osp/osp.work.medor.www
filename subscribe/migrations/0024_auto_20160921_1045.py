# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations


def fix_missing_confirmation_date(apps, schema_editor):
    dt = datetime.datetime(2015, 12, 31)
    Order = apps.get_model("subscribe", "Order")
    Order.objects.filter(status=1, confirmation_date=None).update(confirmation_date=dt)


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0023_auto_20160921_0946'),
    ]

    operations = [
        migrations.RunPython(fix_missing_confirmation_date),
    ]
