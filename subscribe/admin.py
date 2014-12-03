# -*- coding: utf-8 -*-
from django.contrib import admin
from django.core.mail import send_mass_mail
from django.template.loader import render_to_string
from subscribe.models import Subscription, Cooperation


def subscription_reminder_first(modeladmin, request, queryset):
    emails = []

    for obj in queryset:
        subject = "Médor SCRL FS. Détails de votre paiement"
        message = render_to_string('subscribe/subscription-reminder-first.txt', {'obj': obj})
        sender = "lesyeuxouverts@medor.coop"
        recipients = [obj.email]
        emails.append((subject, message, sender, recipients))

    send_mass_mail(emails, fail_silently=False)

subscription_reminder_first.short_description = "Envoyer un premier rappel abonné par email"


def subscription_reminder_second(modeladmin, request, queryset):
    emails = []

    for obj in queryset:
        subject = "Médor SCRL FS. Détails de votre paiement"
        message = render_to_string('subscribe/subscription-reminder-second.txt', {'obj': obj})
        sender = "lesyeuxouverts@medor.coop"
        recipients = [obj.email]
        emails.append((subject, message, sender, recipients))

    send_mass_mail(emails, fail_silently=False)

subscription_reminder_second.short_description = "Envoyer un second rappel abonné par email"


def cooperation_reminder_first(modeladmin, request, queryset):
    emails = []

    for obj in queryset:
        subject = "Médor SCRL FS. Détails de votre paiement"
        message = render_to_string('subscribe/cooperation-reminder-first.txt', {'obj': obj})
        sender = "lesyeuxouverts@medor.coop"
        recipients = [obj.email]
        emails.append((subject, message, sender, recipients))

    send_mass_mail(emails, fail_silently=False)

cooperation_reminder_first.short_description = "Envoyer un premier rappel coopérateur par email"


def cooperation_reminder_second(modeladmin, request, queryset):
    emails = []

    for obj in queryset:
        subject = "Médor SCRL FS. Détails de votre paiement"
        message = render_to_string('subscribe/cooperation-reminder-second.txt', {'obj': obj})
        sender = "lesyeuxouverts@medor.coop"
        recipients = [obj.email]
        emails.append((subject, message, sender, recipients))

    send_mass_mail(emails, fail_silently=False)

cooperation_reminder_second.short_description = "Envoyer un second rappel coopérateur par email"


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'status', 'email', 'invoice_reference', 'structured_communication', 'old_structured_communication', 'country')
    list_filter = ('status', 'country')
    list_editable = ('status',)
    date_hierarchy = 'creation_date'
    search_fields = ('first_name', 'last_name', 'status', 'email', 'invoice_reference')
    actions = [subscription_reminder_first, subscription_reminder_second]


class CooperationAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'status', 'email', 'share_number', 'invoice_reference', 'structured_communication', 'old_structured_communication', 'country')
    list_filter = ('status', 'country')
    list_editable = ('status',)
    date_hierarchy = 'creation_date'
    search_fields = ('first_name', 'last_name', 'status', 'email', 'invoice_reference')
    actions = [cooperation_reminder_first, cooperation_reminder_second]


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Cooperation, CooperationAdmin)
