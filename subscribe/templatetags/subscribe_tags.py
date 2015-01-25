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


@register.assignment_tag
def get_next_events():
    import datetime
    import pytz
    import requests
    from icalendar import Calendar


    request = requests.get('http://dav.medor.coop/medor/medor-evenements.ics/', auth=('medor', 'felix'))
    request.encoding = 'UTF-8'

    gcal = Calendar.from_ical(request.text)

    events = [c for c in gcal.walk() if c.name == 'VEVENT']


    def to_datetime(dt):
        if isinstance(dt, datetime.date):
            return datetime.datetime.combine(dt, datetime.time(0, 0)).replace(tzinfo=pytz.timezone('Europe/Brussels'))
        else:
            return dt


    def compare(item1, item2):
        item1 = to_datetime(item1)
        item2 = to_datetime(item2)

        if item1 == item2:
            return 0
        elif item1 < item2:
            return -1
        else:
            return 1

    events.sort(key=lambda r: r.get('dtstart').dt, cmp=compare)

    now = datetime.datetime.now()
    now = now.replace(tzinfo=pytz.timezone('Europe/Brussels'))
    yesterday = now - datetime.timedelta(1)
    events = [e for e in events if to_datetime(e.get('dtstart').dt) > yesterday]

    return events[:3]
