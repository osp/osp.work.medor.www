# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def fix_creation_date(apps, schema_editor):
    Subscription = apps.get_model("subscribe", "Subscription")
    Order = apps.get_model("subscribe", "Order")

    for subscription in Subscription.objects.all():
        order = Order.objects.get(invoice_reference=subscription.invoice_reference)
        order.creation_date = subscription.creation_date
        order.save()


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0022_auto_20160919_0013'),
    ]

    operations = [
        migrations.RunPython(fix_creation_date),
    ]
