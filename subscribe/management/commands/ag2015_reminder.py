 # -*- coding: utf-8 -*-

from django.core.management.base import BaseCommand, CommandError
from subscribe.models import Cooperation
import itertools
from django.core.mail import send_mass_mail
from django.template.loader import render_to_string
import time


def mygrouper(n, iterable):
    args = [iter(iterable)] * n
    return ([e for e in t if e != None] for t in itertools.izip_longest(*args))


class Command(BaseCommand):
    help = 'Sends a reminder to the cooperators for the 2015 AG'

    def handle(self, *args, **options):
        emails = Cooperation.objects.values_list('email', flat=True).distinct()
        to_go = len(emails)

        for group in mygrouper(10, emails):
            print(group)
            print(to_go)
            messages = []
            for email in group:
                subject = "Rappel : inscription à l'Assemblée Générale Médor 2015"
                message = render_to_string('subscribe/cooperation-ag2015-reminder.txt', {})
                sender = "lesyeuxouverts@medor.coop"
                recipients = [email]
                messages.append((subject, message, sender, recipients))

            send_mass_mail(messages, fail_silently=False)
            to_go -= 10
            time.sleep(5)
