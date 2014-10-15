# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from subscribe.models import Subscription, Cooperation


def subscription_reminder(modeladmin, request, queryset):
    for i in queryset:
        subject = "Médor SCRL FS. Détails de votre paiement"
        message = render_to_string('subscribe/subscription-reminder.txt', {
            'data': i,
            'amount': 60 * i.share_number,
        })
        sender = "medor@medor.coop"
        recipients = [i.email]
        send_mail(subject, message, sender, recipients)
subscription_reminder.short_description = "Envoyer un rappel abonné par email"


def cooperation_reminder(modeladmin, request, queryset):
    for i in queryset:
        subject = "Médor SCRL FS. Détails de votre paiement"
        message = render_to_string('subscribe/subscription-reminder.txt', {
            'data': i,
        })
        sender = "medor@medor.coop"
        recipients = [i.email]
        send_mail(subject, message, sender, recipients)
cooperation_reminder.short_description = "Envoyer un rappel coopérateur par email"


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'status', 'email', 'invoice_reference', 'structured_communication')
    list_filter = ('status',)
    list_editable = ('status',)
    #actions = [subscription_reminder]


class CooperationAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'status', 'email', 'share_number', 'invoice_reference', 'structured_communication')
    list_filter = ('status',)
    list_editable = ('status',)
    date_hierarchy = 'creation_date'
    #actions = [cooperation_reminder]


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Cooperation, CooperationAdmin)
