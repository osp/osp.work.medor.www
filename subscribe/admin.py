# -*- coding: utf-8 -*-

import unicodecsv

from django.contrib import admin
from django.core.mail import send_mass_mail
from django.http import HttpResponse
from django.template.loader import render_to_string

from subscribe.models import Subscription, Cooperation, Order, Item, ItemMembership, ShippingDetails, Offer, Sponsorship


#  def subscription_reminder_first(modeladmin, request, queryset):
#      emails = []

#      for obj in queryset:
#          subject = "Médor SCRL FS. Détails de votre paiement"
#          message = render_to_string('subscribe/subscription-reminder-first.txt', {'obj': obj})
#          sender = "lesyeuxouverts@medor.coop"
#          recipients = [obj.email]
#          emails.append((subject, message, sender, recipients))

#      send_mass_mail(emails, fail_silently=False)

#  subscription_reminder_first.short_description = "Envoyer un premier rappel abonné par email"


#  def subscription_reminder_second(modeladmin, request, queryset):
#      emails = []

#      for obj in queryset:
#          subject = "Médor SCRL FS. Détails de votre paiement"
#          message = render_to_string('subscribe/subscription-reminder-second.txt', {'obj': obj})
#          sender = "lesyeuxouverts@medor.coop"
#          recipients = [obj.email]
#          emails.append((subject, message, sender, recipients))

#      send_mass_mail(emails, fail_silently=False)

#  subscription_reminder_second.short_description = "Envoyer un second rappel abonné par email"


#  def subscription_present(modeladmin, request, queryset):
#      emails = []

#      for obj in queryset:
#          subject = "Médor n'est pas un chien. C'est un cadeau."
#          message = render_to_string('subscribe/subscription-present.txt', {})
#          sender = "lesyeuxouverts@medor.coop"
#          recipients = [obj.email]
#          emails.append((subject, message, sender, recipients))

#      send_mass_mail(emails, fail_silently=False)

#  subscription_present.short_description = "Envoyer l'offre Noël par email"


#  def cooperation_ag_2015_invitation(modeladmin, request, queryset):
#      emails = []

#      for obj in queryset:
#          subject = "Invitation à l'Assemblée Générale Médor 2015"
#          message = render_to_string('subscribe/cooperation-ag2015-invitation.txt', {'obj': obj})
#          sender = "lesyeuxouverts@medor.coop"
#          recipients = [obj.email]
#          emails.append((subject, message, sender, recipients))

#      send_mass_mail(emails, fail_silently=False)

#  cooperation_ag_2015_invitation.short_description = "Envoyer une invitation à l'AG 2015 (version 1er mai 2015)"


#  def cooperation_ag_2015(modeladmin, request, queryset):
#      emails = []

#      for obj in queryset:
#          subject = "Invitation à l'Assemblée Générale Médor 2015"
#          message = render_to_string('subscribe/cooperation-ag2015.txt', {'obj': obj})
#          sender = "lesyeuxouverts@medor.coop"
#          recipients = [obj.email]
#          emails.append((subject, message, sender, recipients))

#      send_mass_mail(emails, fail_silently=False)

#  cooperation_ag_2015.short_description = "Envoyer une invitation à l'AG 2015"


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


#  def cooperation_present(modeladmin, request, queryset):
#      emails = []

#      for obj in queryset:
#          subject = "Médor n'est pas un chien. C'est un cadeau."
#          message = render_to_string('subscribe/cooperation-present.txt', {'obj': obj})
#          sender = "lesyeuxouverts@medor.coop"
#          recipients = [obj.email]
#          emails.append((subject, message, sender, recipients))

#      send_mass_mail(emails, fail_silently=False)

#  cooperation_present.short_description = "Envoyer l'offre Noël par email"


class AlsoCooperatorListFilter(admin.SimpleListFilter):
    title = 'also cooperator'
    parameter_name = 'also_cooperator'

    def lookups(self, request, model_admin):
        return (
            (1, 'oui'),
            (0, 'non')
        )

    def queryset(self, request, queryset):
        if self.value() == "1":
            valid_emails = Cooperation.objects.values_list('email', flat=True).distinct()
            return queryset.filter(email__in=valid_emails)

        if self.value() == "0":
            valid_emails = Cooperation.objects.values_list('email', flat=True).distinct()
            return queryset.exclude(email__in=valid_emails)


#  class SubscriptionAdmin(admin.ModelAdmin):
#      list_display = ('__unicode__', 'status', 'from_issue', 'email', 'invoice_reference', 'structured_communication', 'country', 'creation_date', 'confirmation_date')
#      list_filter = ('status', 'from_issue', AlsoCooperatorListFilter, 'country')
#      list_editable = ('status', 'from_issue')
#      date_hierarchy = 'creation_date'
#      readonly_fields = ('creation_date',)
#      search_fields = ('first_name', 'last_name', 'status', 'email', 'invoice_reference')
#      fieldsets = (
#          (None, {
#              'fields': (
#                  'title',
#                  ('first_name', 'last_name'),
#                  'email',
#                  ('status', 'from_issue', 'creation_date', 'confirmation_date'),
#                  'invoice_reference',
#                  'comment'
#              )
#          }),
#          ('Infos', {
#              'classes': ('collapse',),
#              'fields': (
#                  'street',
#                  'number',
#                  'letterbox',
#                  'city',
#                  'zip_code',
#                  'country'
#              )
#          }),
#          ('Destinataire', {
#              'classes': ('collapse',),
#              'fields': (
#                  'is_gift',
#                  'recipient_title',
#                  'recipient_first_name',
#                  'recipient_last_name',
#                  'recipient_email'
#              )
#          }),
#      )
#      actions = [subscription_reminder_first, subscription_reminder_second, subscription_present]


class AlsoSubscriberListFilter(admin.SimpleListFilter):
    title = 'also subscriber'
    parameter_name = 'also_subscriber'

    def lookups(self, request, model_admin):
        return (
            (1, 'oui'),
            (0, 'non')
        )

    def queryset(self, request, queryset):
        if self.value() == "1":
            valid_emails = Subscription.objects.values_list('email', flat=True).distinct()
            return queryset.filter(email__in=valid_emails)

        if self.value() == "0":
            valid_emails = Subscription.objects.values_list('email', flat=True).distinct()
            return queryset.exclude(email__in=valid_emails)


class CooperationAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'status', 'email', 'share_number', 'invoice_reference', 'structured_communication', 'old_structured_communication', 'country')
    list_filter = ('status', 'country', AlsoSubscriberListFilter)
    list_editable = ('status',)
    date_hierarchy = 'creation_date'
    search_fields = ('first_name', 'last_name', 'status', 'email', 'invoice_reference')
    actions = [
        cooperation_reminder_first,
        cooperation_reminder_second,
        #  cooperation_present,
        #  cooperation_ag_2015,
        #  cooperation_ag_2015_invitation
    ]


class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('__unicode__', 'is_published', 'transaction_type', 'price')
    list_filter = ('is_published', 'transaction_type',)


class ItemMembershipAdmin(admin.ModelAdmin):
    model = ItemMembership
    list_display = ('__unicode__', 'quantity', 'order_status', 'is_shipped', 'order')
    list_filter = ('is_shipped', 'order__status', 'item')
    list_editable = ('is_shipped',)
    actions = ['subscription_reminder_first', 'export_as_csv']

    def subscription_reminder_first(self, request, queryset):
        emails = []

        for obj in queryset:
            subject = "Médor SCRL FS. Rappel de paiement"
            message = render_to_string('subscribe/subscription-reminder-first.txt', {'obj': obj.order})
            sender = "medor@medor.coop"
            recipients = [obj.order.email]
            emails.append((subject, message, sender, recipients))

        send_mass_mail(emails, fail_silently=False)

    subscription_reminder_first.short_description = "Envoyer un premier rappel abonné par email"

    def export_as_csv(self, request, queryset):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="lignes-de-commandes.csv"'

        writer = unicodecsv.writer(response, encoding='utf-8')
        writer.writerow([
            u"Quantité",
            u"Description",
            u"Nom",
            u"Prénom",
            u"Courriel",
            u"Organisation",
            u"Status",
            u"Est un cadeau?",
            u"Pour Nom,",
            u"Pour Prénom",
            u"Pour Courriel",
            u"Adresse",
            u"Boîte",
            u"Code postal",
            u"Ville",
            u"Pays",
            u"Date de création",
            u"Date de confirmation",
            u"Référence",
            u"Communication",
        ])

        for im in queryset:
            o = im.order
            d = o.shipping_details

            writer.writerow([
                im.quantity,
                im.item.name,
                o.last_name,
                o.first_name,
                o.email,
                o.organization or u"-",
                o.get_status_display(),
                o.is_gift,
                d.first_name,
                d.last_name,
                d.email,
                u"{}, {}".format(d.street, d.number),
                d.box,
                d.postcode,
                d.city,
                d.country,
                o.creation_date,
                o.confirmation_date,
                o.invoice_reference,
                o.structured_communication(),
            ])

        return response

    export_as_csv.short_description = "Exporter en CSV"


class ItemMembershipInline(admin.TabularInline):
    model = ItemMembership


class ShippingDetailsAdmin(admin.ModelAdmin):
    pass


class OrderAdmin(admin.ModelAdmin):
    inlines = (ItemMembershipInline,)
    list_display = ('__unicode__', 'grand_total', 'creation_date', 'status', 'confirmation_date', 'structured_communication', 'items_as_list')
    list_editable = ('status',)
    list_filter = ('status', 'shipping_details__country')
    date_hierarchy = 'confirmation_date'
    readonly_fields = ('creation_date', 'confirmation_date', 'invoice_reference', 'structured_communication', 'grand_total')
    search_fields = ('first_name', 'last_name', 'status', 'email', 'invoice_reference')
    actions = ['export_as_csv', 'reminder_first', 'reminder_second']

    def export_as_csv(self, request, queryset):
        # Create the HttpResponse object with the appropriate CSV header.
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="commandes.csv"'

        writer = unicodecsv.writer(response, encoding='utf-8')
        writer.writerow([
            u"Nom",
            u"Prénom",
            u"Courriel",
            u"Organisation",
            u"Status",
            u"Est un cadeau?",
            u"Pour Nom,",
            u"Pour Prénom",
            u"Pour Courriel",
            u"Adresse",
            u"Boîte",
            u"Code postal",
            u"Ville",
            u"Pays",
            u"Date de création",
            u"Date de confirmation",
            u"Référence",
            u"Communication",
            u"Produits",
        ])

        for o in queryset:
            d = o.shipping_details
            im = o.itemmembership_set.values_list('item__name', 'quantity')

            writer.writerow([
                o.last_name,
                o.first_name,
                o.email,
                o.organization or u"-",
                o.get_status_display(),
                o.is_gift,
                d.first_name,
                d.last_name,
                d.email,
                u"{}, {}".format(d.street, d.number),
                d.box,
                d.postcode,
                d.city,
                d.country,
                o.creation_date,
                o.confirmation_date,
                o.invoice_reference,
                o.structured_communication(),
                u" + ".join([u"{} (x{})".format(*i) for i in im])
            ])

        return response

    export_as_csv.short_description = "Exporter en CSV"

    def reminder_first(modeladmin, request, queryset):
        emails = []

        for obj in queryset:
            subject = "Médor SCRL FS. Détails de votre paiement"
            message = render_to_string('subscribe/order-reminder-first.txt', {'obj': obj})
            sender = "medor@medor.coop"
            recipients = [obj.email]
            emails.append((subject, message, sender, recipients))

        send_mass_mail(emails, fail_silently=False)

    reminder_first.short_description = "Envoyer un premier rappel abonné par email"

    def reminder_second(modeladmin, request, queryset):
        emails = []

        for obj in queryset:
            subject = "Médor SCRL FS. Détails de votre paiement"
            message = render_to_string('subscribe/order-reminder-second.txt', {'obj': obj})
            sender = "medor@medor.coop"
            recipients = [obj.email]
            emails.append((subject, message, sender, recipients))

        send_mass_mail(emails, fail_silently=False)

    reminder_second.short_description = "Envoyer un second rappel abonné par email"


class OfferAdmin(admin.ModelAdmin):
    pass


class SponsorshipAdmin(admin.ModelAdmin):
    pass


#admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Cooperation, CooperationAdmin)

admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ItemMembership, ItemMembershipAdmin)
admin.site.register(ShippingDetails, ShippingDetailsAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Sponsorship, SponsorshipAdmin)
