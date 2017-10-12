# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import caldav
import datetime
import pytz

from django import template
from django.db.models import Sum
from subscribe.models import Subscription, Cooperation
from django.conf import settings


register = template.Library()


@register.assignment_tag
def get_subscriber_count():
    return Subscription.objects.exclude(status=2).count()


@register.assignment_tag
def get_capital_amount():
    return Cooperation.objects.exclude(status=2).aggregate(total=Sum('share_number'))['total'] * 20


def _get_next_events():

    def sort_key_func(x):
        val = getattr(x.instance.vevent, 'dtstart', None)
        if not val:
            return None
        val = val.value
        if hasattr(val, 'strftime'):
            return val.strftime('%F%H%M%S')
            return val.strftime('%F%H%M%S')

    url = settings.CALDAV_URL
    client = caldav.DAVClient(url)
    principal = client.principal()
    cal = principal.calendar(cal_id=settings.CALDAV_CAL_ID)

    now = datetime.datetime.now()
    now = now.replace(tzinfo=pytz.timezone(settings.TIME_ZONE))

    events = cal.date_search(now)
    events.sort(key=sort_key_func)

    return [e.instance.vevent for e in events[:4]]


@register.assignment_tag
def get_next_events():
    try:
        events = _get_next_events()
    except:
        events = []

    return events
