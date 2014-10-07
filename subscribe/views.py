# -*- coding: utf-8 -*-
from django.contrib.formtools.wizard.views import CookieWizardView
from django.core.mail import send_mail
from django.db.models import Sum
from django.shortcuts import render
from django.template.loader import render_to_string
from django.views.generic.base import TemplateView

from subscribe.forms import CooperationForm, SubscriptionForm, ConfirmForm
from subscribe.models import Subscription, Cooperation


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

        subject = "Médor SCRL FS. Détails de votre paiement"
        message = render_to_string('subscribe/cooperation-email.txt', {
                'data': form_list[0].cleaned_data,
                'amount': form_list[0].cleaned_data['share_number'] * 20,
                'communication': form_list[0].instance.structured_communication(),
            })
        sender = "medor@medor.coop"
        recipients = [form_list[0].cleaned_data['email']]
        send_mail(subject, message, sender, recipients)

        return render(self.request, 'subscribe/cooperation-done.html', {
            'communication': form_list[0].instance.structured_communication(),
            'form_data': [form.cleaned_data for form in form_list],
            'amount': form_list[0].cleaned_data['share_number'] * 20,
        })


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

        subject = "Médor SCRL FS. Détails de votre paiement"
        message = render_to_string('subscribe/subscription-email.txt', {
                'data': form_list[0].cleaned_data,
                'amount': 60,
                'communication': form_list[0].instance.structured_communication(),
            })
        sender = "medor@medor.coop"
        recipients = [form_list[0].cleaned_data['email']]
        send_mail(subject, message, sender, recipients)

        return render(self.request, 'subscribe/subscription-done.html', {
            'communication': form_list[0].instance.structured_communication(),
            'form_data': [form.cleaned_data for form in form_list],
        })


class HomePageView(TemplateView):
    template_name = "subscribe/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['subscriber_count'] = Subscription.objects.count()
        context['cooperative_money'] = Cooperation.objects.aggregate(Sum('share_number'))['share_number__count'] * 20
        return context


class FAQPageView(TemplateView):
    template_name = "subscribe/FAQ.html"
