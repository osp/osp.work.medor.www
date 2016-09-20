# -*- coding: utf-8 -*-
from formtools.wizard.views import CookieWizardView

from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string

from subscribe.forms import CooperationForm, SubscriptionForm, ConfirmForm, ItemChoiceForm, DetailsForm, ConfirmForm2
from subscribe.models import Subscription, Cooperation, Order, ItemMembership

import unicodecsv
from django.http import HttpResponse
from django.contrib.auth.decorators import user_passes_test


COOPERATION_FORMS = [
    CooperationForm,
    ConfirmForm,
]

COOPERATION_TEMPLATES = [
    "subscribe/cooperation-registration.html",
    "subscribe/cooperation-verification.html",
]


SUBSCRIPTION_FORMS = [
    SubscriptionForm,
    ConfirmForm,
]

SUBSCRIPTION_TEMPLATES = [
    "subscribe/subscription-registration.html",
    "subscribe/subscription-verification.html",
]


class CooperationWizardView(CookieWizardView):
    form_list = COOPERATION_FORMS

    def get_context_data(self, form, **kwargs):
        context = super(CooperationWizardView, self).get_context_data(form=form, **kwargs)
        if self.steps.current == '1':
            context.update({
                'infos': self.get_cleaned_data_for_step("0"),
                'amount': self.get_cleaned_data_for_step("0")['share_number'] * 20
            })
        return context

    def get_template_names(self):
        return [COOPERATION_TEMPLATES[int(self.steps.current)]]

    def done(self, form_list, form_dict, **kwargs):
        form_list[0].save()
        obj = form_list[0].instance

        subject = "Médor SCRL FS. Détails de votre paiement"
        message = render_to_string('subscribe/cooperation-email.txt', {'obj': obj})
        sender = "lesyeuxouverts@medor.coop"
        recipients = [obj.email]
        send_mail(subject, message, sender, recipients)

        return render(self.request, 'subscribe/cooperation-done.html', {'obj': obj})


class SubscriptionWizardView(CookieWizardView):
    form_list = SUBSCRIPTION_FORMS

    def get_context_data(self, form, **kwargs):
        context = super(SubscriptionWizardView, self).get_context_data(form=form, **kwargs)
        if self.steps.current == '1':
            context.update({
                'infos': self.get_cleaned_data_for_step("0"),
            })
        return context

    def get_template_names(self):
        return [SUBSCRIPTION_TEMPLATES[int(self.steps.current)]]

    def done(self, form_list, form_dict, **kwargs):
        form_list[0].save()
        obj = form_list[0].instance

        subject = "Médor SCRL FS. Détails de votre paiement"
        message = render_to_string('subscribe/subscription-email.txt', {'obj': obj})
        sender = "lesyeuxouverts@medor.coop"
        recipients = [obj.email]
        send_mail(subject, message, sender, recipients)

        return render(self.request, 'subscribe/subscription-done.html', {'obj': obj})


def can_read_csv(user):
    """docstring for can_read_proposals"""
    return user.groups.filter(name='Accounting').exists()


@user_passes_test(can_read_csv)
def subscribers_as_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="subscribers.csv"'

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

    for o in Order.objects.all():
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


@user_passes_test(can_read_csv)
def cooperators_as_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="cooperators.csv"'

    writer = unicodecsv.writer(response, encoding='utf-8')
    writer.writerow([
        "email",
        "title",
        "last name",
        "first name",
        "phone number",
        "address",
        "letter box",
        "city",
        "zip code",
        "country",
        "founder",
        "newsletter",
        "subscriber",
        "cooperator",
        "author",
        "function",
        "organisation",
        "encoder",
        "creation date",
        "confirmation date",
        "comment",
        "invoice reference",
        "structured communication",
        "status",
        "share number"
    ])

    for s in Cooperation.objects.all():
        writer.writerow([
            s.email,
            s.get_title_display(),
            s.last_name,
            s.first_name,
            "",
            u"{}, {}".format(s.street, s.number),
            s.letterbox,
            s.city,
            s.zip_code,
            s.country,
            "false",  # fondeur
            "false",  # newsletter
            "false",  # subscriber
            "true",  # cooperator
            "false",  # author
            "",  # fonction
            "",  # organisation
            "medor.coop",  # encodeur
            s.creation_date,
            s.confirmation_date,
            u"{} part(s)".format(s.share_number),  # comment
            s.invoice_reference,
            s.structured_communication(),
            s.get_status_display(),
            u"{}".format(s.share_number),
        ])

    return response


class OrderWizardView(CookieWizardView):
    TEMPLATES = [
        "subscribe/order-selection.html",
        "subscribe/order-details.html",
        "subscribe/order-confirmation.html",
    ]

    form_list = [
        ItemChoiceForm,
        DetailsForm,
        ConfirmForm2,
    ]

    def get_context_data(self, form, **kwargs):
        context = super(OrderWizardView, self).get_context_data(form=form, **kwargs)

        if self.steps.current in ['1', '2']:
            context.update({
                'infos': self.get_cleaned_data_for_step("0"),
            })

        if self.steps.current == '2':
            context.update({
                'infos2': self.get_cleaned_data_for_step("1"),
            })

        return context

    def get_template_names(self):
        return self.TEMPLATES[int(self.steps.current)]

    def done(self, form_list, form_dict, **kwargs):
        item_choice_form = form_list[0]
        details_form = form_list[1]

        # Créer le Shippingdetails
        details = details_form.save()

        # Créer le order
        order = Order()
        order.shipping_details = details
        order.first_name = details_form.cleaned_data["order_first_name"]
        order.last_name = details_form.cleaned_data["order_last_name"]
        order.email = details_form.cleaned_data["order_email"]
        order.is_gift = details_form.cleaned_data["order_is_gift"]
        order.save()

        # Créer les itemmembership
        for i in item_choice_form.cleaned_data["per_items"]:
            im = ItemMembership(item=i, order=order, quantity=1)
            im.save()

        for i in item_choice_form.cleaned_data["subscriptions"]:
            im = ItemMembership(item=i, order=order, quantity=1)
            im.save()

        #  sends an email with the order details
        order.send_details_email()

        return render(self.request, 'subscribe/order-done.html', {'obj': order})
