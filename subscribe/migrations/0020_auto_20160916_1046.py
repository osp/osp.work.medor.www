# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0019_auto_20160916_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingdetails',
            name='letterbox',
        ),
        migrations.RemoveField(
            model_name='shippingdetails',
            name='zip_code',
        ),
    ]
