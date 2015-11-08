# -*- coding: utf-8 -*-
from django.contrib.formtools.wizard.views import CookieWizardView
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string

from subscribe.forms import CooperationForm, SubscriptionForm, ConfirmForm
from subscribe.models import Subscription, Cooperation

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

        subject = "Invitation à l'Assemblée Générale Médor 2015"
        message = render_to_string('subscribe/cooperation-ag2015-invitation.txt', {})
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
        "is_gift",
        "recipient_title",
        "recipient_first_name",
        "recipient_last_name",
        "recipient_email",
        "founder",
        "newsletter",
        "subscriber",
        "cooperator",
        "author",
        "function",
        "organisation",
        "encoder",
        "creation date",
        "comment",
        "invoice reference",
        "structured communication",
        "status",
    ])

    for s in Subscription.objects.all():
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
            s.is_gift,
            s.get_recipient_title_display(),
            s.recipient_first_name or s.first_name,
            s.recipient_last_name or s.last_name,
            s.recipient_email or s.email,
            "false", #fondeur
            "false", #newsletter
            "true", #subscriber
            "false", #cooperator
            "false", #author
            "", #fonction
            "", #organisation
            "medor.coop", #encodeur
            s.creation_date,
            "", #comment
            s.invoice_reference,
            s.structured_communication(),
            s.get_status_display(),
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
            "false", #fondeur
            "false", #newsletter
            "false", #subscriber
            "true", #cooperator
            "false", #author
            "", #fonction
            "", #organisation
            "medor.coop", #encodeur
            s.creation_date,
            u"{} part(s)".format(s.share_number), #comment
            s.invoice_reference,
            s.structured_communication(),
            s.get_status_display(),
            u"{}".format(s.share_number),
        ])

    return response
