# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


def populate_box_postcode(apps, schema_editor):
    ShippingDetails = apps.get_model("subscribe", "ShippingDetails")
    for details in ShippingDetails.objects.all():
        details.box = details.letterbox if details.letterbox else ""
        details.postcode = details.zip_code if details.zip_code else ""
        details.save()


def populate_organization(apps, schema_editor):
    Order = apps.get_model("subscribe", "Order")
    for order in Order.objects.all():
        order.organization = ""
        order.save()


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0018_auto_20160916_1036'),
    ]

    operations = [
        migrations.RunPython(populate_box_postcode),
        migrations.RunPython(populate_organization),
    ]
