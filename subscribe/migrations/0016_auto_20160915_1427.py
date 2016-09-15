# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    def populate_items(apps, schema_editor):
        Subscription = apps.get_model("subscribe", "Subscription")
        Item = apps.get_model("subscribe", "Item")

        from_issues = filter(None, set(Subscription.objects.values_list('from_issue', flat=True)))

        for issue in from_issues:
            txt = u", ".join([str(x) for x in range(issue, issue + 4)])
            item = Item(transaction_type=1, price=60, name="Abonnement 1 an (%s)" % txt)
            item.save()

    def recreate_subscriptions(apps, schema_editor):
        Subscription = apps.get_model("subscribe", "Subscription")
        Item = apps.get_model("subscribe", "Item")
        ItemMembership = apps.get_model("subscribe", "ItemMembership")
        Order = apps.get_model("subscribe", "Order")
        ShippingDetails = apps.get_model("subscribe", "ShippingDetails")

        for subscription in Subscription.objects.all():
            details = ShippingDetails()
            details.first_name = subscription.recipient_first_name or subscription.first_name
            details.last_name = subscription.recipient_last_name or subscription.last_name
            details.email = subscription.recipient_email or subscription.email
            details.street = subscription.street
            details.number = subscription.number
            details.letterbox = subscription.letterbox
            details.city = subscription.city
            details.zip_code = subscription.zip_code
            details.country = subscription.country
            details.save()

            order = Order()
            order.shipping_details = details
            order.first_name = subscription.first_name
            order.last_name = subscription.last_name
            order.email = subscription.email
            order.creation_date = subscription.creation_date
            order.confirmation_date = subscription.confirmation_date
            order.comment = subscription.comment
            order.status = subscription.status
            order.invoice_reference = subscription.invoice_reference
            order.is_gift = subscription.is_gift
            order.save()

            issue = subscription.from_issue
            if issue:
                txt = u", ".join([str(x) for x in range(issue, issue + 4)])
                item = Item.objects.get(name="Abonnement 1 an (%s)" % txt)
                item_member = ItemMembership()
                item_member.item = item
                item_member.order = order
                item_member.quantity = 1
                order.amount = 60 if subscription.country == "BE" else 80
                order.save()
                item_member.save()

    dependencies = [
        ('subscribe', '0015_auto_20160915_1427'),
    ]

    operations = [
        migrations.RunPython(populate_items),
        migrations.RunPython(recreate_subscriptions),
    ]
