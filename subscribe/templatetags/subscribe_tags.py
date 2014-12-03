from django import template
from django.db.models import Sum
from subscribe.models import Subscription, Cooperation


register = template.Library()


@register.assignment_tag
def get_subscriber_count():
    return Subscription.objects.count()


@register.assignment_tag
def get_capital_amount():
    return Cooperation.objects.exclude(status=2).aggregate(total=Sum('share_number'))['total'] * 20
