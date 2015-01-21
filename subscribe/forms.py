# -*- coding: utf-8 -*-
from django import forms
from subscribe.models import Cooperation, Subscription


SUBSCRIPTION_COUNTRY_CHOICES = (
    ('BE', u'Belgique'),
    ('Europe (+ 20 €)', (
            ('AL', 'Albanie'),
            ('PT-20', 'Açores'),
            ('DE', 'Allemagne'),
            ('AD', 'Andorre'),
            ('AT', 'Autriche'),
            ('BY', 'Biélorussie'),
            ('BA', 'Bosnie-Herzégovine'),
            ('BG', 'Bulgarie'),
            ('IC', 'Canaries (Îles)'),
            ('ES-CE', 'Ceuta'),
            ('CY', 'Chypre'),
            ('HR', 'Croatie'),
            ('DK', 'Danemark'),
            ('ES', 'Espagne'),
            ('EE', 'Estonie'),
            ('FO', 'Féroé (Îles)'),
            ('FI', 'Finlande'),
            ('FR', 'France (sauf DOM-TOM)'),
            ('GE', 'Géorgie'),
            ('GI', 'Gibraltar'),
            ('GB', 'Grande-Bretagne'),
            ('GR', 'Grèce'),
            ('GL', 'Groenland'),
            ('GG', 'Guernesey'),
            ('HU', 'Hongrie'),
            ('IE', 'Irlande'),
            ('IS', 'Islande'),
            ('IT', 'Italie'),
            ('JE', 'Jersey'),
            ('LV', 'Lettonie'),
            ('LI', 'Liechtenstein'),
            ('LT', 'Lituanie'),
            ('LU', 'Luxembourg (Grand-Duché de)'),
            ('MK', 'Macédoine'),
            ('PT-30', 'Madère'),
            ('MT', 'Malte'),
            ('IM', 'Man (Île de)'),
            ('Me', 'Melilla'),
            ('MD', 'Moldavie'),
            ('MC', 'Monaco'),
            ('ME', 'Monténégro'),
            ('NO', 'Norvège'),
            ('NL', 'Pays-Bas'),
            ('PL', 'Pologne'),
            ('PT', 'Portugal'),
            ('CZ', 'République tchèque'),
            ('RO', 'Roumanie'),
            ('RU', 'Russie'),
            ('SM', 'Saint-Martin'),
            ('RS', 'Serbie'),
            ('SK', 'Slovaquie'),
            ('SI', 'Slovénie'),
            ('SE', 'Suède'),
            ('CH', 'Suisse'),
            ('TR', 'Turquie'),
            ('UA', 'Ukraine'),
            ('VA', 'Vatican')
        )
    )
)


class ConfirmForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(ConfirmForm, self).__init__(*args, **kwargs)

    error_css_class = 'error'
    required_css_class = 'required'

    confirm = forms.BooleanField(label="Je confirme")


class CooperationForm(forms.ModelForm):
    """
    http://stackoverflow.com/questions/15889794/creating-one-django-form-to-save-two-models
    """
    error_css_class = 'error'
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(CooperationForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Cooperation
        exclude = ('status', 'invoice_reference')
        widgets = {
            'title': forms.RadioSelect(),
            'letterbox': forms.TextInput(),
            'zip_code': forms.TextInput(),
        }


class SubscriptionForm(forms.ModelForm):
    """
    http://stackoverflow.com/questions/15889794/creating-one-django-form-to-save-two-models
    """
    error_css_class = 'error'
    required_css_class = 'required'

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('label_suffix', '')
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        self.fields['country'].choices = SUBSCRIPTION_COUNTRY_CHOICES

    def clean_recipient_first_name(self):
        cleaned_data = super(SubscriptionForm, self).clean()
        is_gift = cleaned_data.get("is_gift")
        recipient_first_name = cleaned_data.get("recipient_first_name")

        if is_gift and not recipient_first_name:
            raise forms.ValidationError("Ce champ est obligatoire.")

        return recipient_first_name

    def clean_recipient_last_name(self):
        cleaned_data = super(SubscriptionForm, self).clean()
        is_gift = cleaned_data.get("is_gift")
        recipient_last_name = cleaned_data.get("recipient_last_name")

        if is_gift and not recipient_last_name:
            raise forms.ValidationError("Ce champ est obligatoire.")

        return recipient_last_name

    class Meta:
        model = Subscription
        exclude = ('status', 'invoice_reference')
        widgets = {
            'title': forms.RadioSelect(),
            'letterbox': forms.TextInput(),
            'zip_code': forms.TextInput(),
            'recipient_title': forms.RadioSelect(),
        }
