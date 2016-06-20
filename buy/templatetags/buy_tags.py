from django import template
from buy.models import RetailOutlet


register = template.Library()


@register.assignment_tag
def get_retail_outlet_list():
    return RetailOutlet.objects.order_by("city")
