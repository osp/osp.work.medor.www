# -*- coding: utf-8 -*-
from django import forms
from django.forms import formset_factory
from subscribe.models import Cooperation, Subscription, Item, ShippingDetails, Order
from subscribe.fields import CustomOrderMultipleChoiceField
from subscribe.widgets import CustomCheckboxSelectMultiple


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


#########################################


class ItemChoiceForm(forms.Form):
    """The form that shows the various Selectable items"""

    error_css_class = 'error'
    required_css_class = 'required'

    subscriptions = CustomOrderMultipleChoiceField(queryset=Item.objects.filter(is_published=True, transaction_type=1),
            widget=CustomCheckboxSelectMultiple(), required=False, label="Je m'abonne")
    per_items = CustomOrderMultipleChoiceField(queryset=Item.objects.filter(is_published=True, transaction_type=2),
            widget=CustomCheckboxSelectMultiple(), required=False, label="J'achète des numéros à la pièce")

    def clean(self):
        """Makes sure that there is at least one selected Item"""

        cleaned_data = super(ItemChoiceForm, self).clean()
        subscriptions = cleaned_data.get("subscriptions")
        per_items = cleaned_data.get("per_items")

        if not subscriptions and not per_items:
            raise forms.ValidationError("Veuillez sélectionner au moins un produit")


class DetailsForm(forms.ModelForm):
    """The customer and shipping details"""

    error_css_class = 'error'
    required_css_class = 'required'

    # TODO: check field option so it matches the model
    order_first_name = forms.CharField(max_length=255, label="prénom")
    order_last_name = forms.CharField(max_length=255, label="nom")
    order_email = forms.EmailField(label="courriel")
    order_email_verification = forms.EmailField(label="vérification du courriel")
    order_is_gift = forms.BooleanField(label="ceci est un cadeau")

    class Meta:
        model = ShippingDetails
        exclude = []

    def clean_order_email(self):
        """Makes sure that the email is correct"""

        cleaned_data = super(ItemChoiceForm, self).clean()
        subscriptions = cleaned_data.get("subscriptions")
        per_items = cleaned_data.get("per_items")

        if not subscriptions and not per_items:
            raise forms.ValidationError("Veuillez sélectionner au moins un produit")
