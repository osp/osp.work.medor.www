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
        exclude = ('status', 'communication')
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

    class Meta:
        model = Subscription
        widgets = {
            'title': forms.RadioSelect(),
            'country': forms.RadioSelect(),
            'letterbox': forms.TextInput(),
            'zip_code': forms.TextInput(),
        }
