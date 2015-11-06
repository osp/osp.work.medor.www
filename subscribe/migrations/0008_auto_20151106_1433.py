# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


STATUS_CONFIRMED = 1

def confirm(apps, schema_editor):
    Subscription = apps.get_model("subscribe", "Subscription")
    for subscription in Subscription.objects.all():
        if subscription.status == STATUS_CONFIRMED:
            subscription.confirmation_date = subscription.creation_date
            subscription.save()

    Cooperation = apps.get_model("subscribe", "Cooperation")
    for cooperation in Cooperation.objects.all():
        if cooperation.status == STATUS_CONFIRMED:
            cooperation.confirmation_date = cooperation.creation_date
            cooperation.save()


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0007_auto_20151106_1139'),
    ]

    operations = [
        migrations.RunPython(confirm),
    ]
