from django import forms
from subscribe.models import Cooperation, Subscription


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
            'country': forms.RadioSelect(),
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

    def clean_recipient_first_name(self):
        cleaned_data = super(SubscriptionForm, self).clean()
        is_gift = cleaned_data.get("is_gift")
        recipient_first_name = cleaned_data.get("recipient_first_name")

        if is_gift and not recipient_first_name:
            raise forms.ValidationError("Ce champ est obligatoire.")

    def clean_recipient_last_name(self):
        cleaned_data = super(SubscriptionForm, self).clean()
        is_gift = cleaned_data.get("is_gift")
        recipient_last_name = cleaned_data.get("recipient_last_name")

        if is_gift and not recipient_last_name:
            raise forms.ValidationError("Ce champ est obligatoire.")

    class Meta:
        model = Subscription
        exclude = ('status', 'invoice_reference')
        widgets = {
            'title': forms.RadioSelect(),
            'country': forms.RadioSelect(),
            'letterbox': forms.TextInput(),
            'zip_code': forms.TextInput(),
        }
