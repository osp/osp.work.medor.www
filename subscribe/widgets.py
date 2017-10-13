from django.forms.widgets import CheckboxSelectMultiple


class CustomCheckboxSelectMultiple(CheckboxSelectMultiple):
    template_name = 'subscribe/widgets/checkbox_select.html'
    option_template_name = 'subscribe/widgets/checkbox_option.html'
