from django import forms
from django.forms.models import model_to_dict, fields_for_model
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
        self.fields['birth_date'].widget.attrs["placeholder"] = "JJ/MM/AAAA"
        self.fields['phone_number'].widget.attrs["placeholder"] = "+32 "

    class Meta:
        model = Cooperation
        exclude = ('status', 'communication')
        widgets = {
            'title': forms.RadioSelect(),
            'nationality': forms.RadioSelect(),
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
        self.fields['phone_number'].widget.attrs["placeholder"] = "+32 "

    class Meta:
        model = Subscription
