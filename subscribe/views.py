# -*- coding: utf-8 -*-
from django.contrib.formtools.wizard.views import CookieWizardView
from django.core.mail import send_mail
from django.shortcuts import render
from django.template.loader import render_to_string

from subscribe.forms import CooperationForm, SubscriptionForm, ConfirmForm
from subscribe.models import Subscription

import unicodecsv
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required



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


@login_required
def subscribers_as_csv(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="subscribers.csv"'

    writer = unicodecsv.writer(response, encoding='utf-8')
    #writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])

    for s in Subscription.objects.all():
        writer.writerow([s.title, s.first_name, s.last_name, s.email, s.street, s.number, s.letterbox, s.city, s.zip_code, s.country, s.creation_date, s.status, s.invoice_reference])

    return response
