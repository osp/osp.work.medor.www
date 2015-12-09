# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from datetime import datetime, date
from django.db.models import Max
from django.template.loader import render_to_string
from django.core.mail import send_mail


TITLE_CHOICES = (
    (False, 'Madame'),
    (True, 'Monsieur')
)


class TransactionBase(models.Model):
    STATUS_CHOICES = (
        (0, 'en cours'),
        (1, 'confirmé'),
        (2, 'annulé')
    )

    COUNTRY_CHOICES = (
        ('AL', 'Albanie'),
        ('PT-20', 'Açores'),
        ('DE', 'Allemagne'),
        ('AD', 'Andorre'),
        ('AT', 'Autriche'),
        ('BE', 'Belgique'),
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

    title = models.BooleanField('civilité', default=False, choices=TITLE_CHOICES)
    first_name = models.CharField('prénom', max_length=30)
    last_name = models.CharField('nom', max_length=30)
    email = models.EmailField('courriel')
    street = models.CharField('rue', max_length=30)
    number = models.CharField('numéro', max_length=50) # 27 bis
    letterbox = models.PositiveSmallIntegerField('boîte postale', max_length=30, null=True, blank=True)
    city = models.CharField('ville', max_length=30)
    zip_code = models.PositiveSmallIntegerField('code postal', max_length=5)
    country = models.CharField('pays', max_length=5, choices=COUNTRY_CHOICES, default="BE")
    creation_date = models.DateTimeField('date de création', auto_now_add=True)
    confirmation_date = models.DateTimeField('date de confirmation du paiement', null=True, blank=True)
    status = models.PositiveSmallIntegerField('statut', choices=STATUS_CHOICES, default=0)
    invoice_reference = models.PositiveIntegerField('référence facture', max_length=10, unique=True, blank=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u"{} {}, {}".format(self.last_name, self.first_name, self.get_title_display())

    def save(self, *args, **kwargs):
        if not self.invoice_reference:
            now = datetime.now()
            _max = self.__class__.objects.filter(creation_date__year=now.year, creation_date__month=now.month).aggregate(Max('invoice_reference'))
            _max = _max['invoice_reference__max']
            if _max:
                _max = _max + 1
                _max = _max % 10000
            else:
                _max = 1

            invoice_reference = u"{}{}{:04d}".format(now.strftime("%y%m"), self.__class__.transaction_type, _max)
            self.invoice_reference = int(invoice_reference)

        super(TransactionBase, self).save(*args, **kwargs)

    def old_simple_communication(self):
        ref = self.invoice_reference
        nbr = "{}{:02d}".format(ref, ref % 97)
        return "{} {} {}".format(nbr[:3], nbr[3:7], nbr[7:])

    def simple_communication(self):
        ref = self.invoice_reference
        modulo = ref % 97
        modulo = modulo if modulo != 0 else 97
        nbr = "{}{:02d}".format(ref, modulo)
        return "{} {} {}".format(nbr[:3], nbr[3:7], nbr[7:])

    def old_structured_communication(self):
        ref = self.invoice_reference
        nbr = "{}{:02d}".format(ref, ref % 97)
        return "+++{}/{}/{}+++".format(nbr[:3], nbr[3:7], nbr[7:])

    def structured_communication(self):
        ref = self.invoice_reference
        modulo = ref % 97
        modulo = modulo if modulo != 0 else 97
        nbr = "{}{:02d}".format(ref, modulo)
        return "+++{}/{}/{}+++".format(nbr[:3], nbr[3:7], nbr[7:])


class Subscription(TransactionBase):
    """ Describes a subscription"""
    ISSUE_CHOICES = (
        (None, '---'),
        (1, 'du 1 au 4'),
        (2, 'du 2 au 5'),
        (3, 'du 3 au 6'),
        (4, 'du 4 au 7')
    )

    transaction_type = '01'
    from_issue = models.PositiveSmallIntegerField('à partir du numéro', choices=ISSUE_CHOICES, blank=True, null=True)
    is_gift = models.BooleanField('ceci est un cadeau?', default=False)
    recipient_title = models.BooleanField('civilité du destinataire', default=False, choices=TITLE_CHOICES)
    recipient_first_name = models.CharField('prénom du destinataire', max_length=30, blank=True)
    recipient_last_name = models.CharField('nom de famille du destinataire', max_length=30, blank=True)
    recipient_email = models.CharField('courriel du destinataire', max_length=30, blank=True)

    class Meta:
        verbose_name = "abonnement"
        verbose_name_plural = "abonnements"

    __original_status = None

    def __init__(self, *args, **kwargs):
        super(Subscription, self).__init__(*args, **kwargs)
        self.__original_status = self.status

    def save(self, *args, **kwargs):
        do_send_mail = False

        if self.status != self.__original_status and self.status == 1:
            # If the status has changed and is confirmed, mark for sending a
            # confirmation email
            do_send_mail = True

        super(Subscription, self).save(*args, **kwargs)
        self.__original_status = self.status

        # Do send the email
        if do_send_mail:
            subject = "Médor SCRL FS. Détails de votre paiement"
            message = render_to_string('subscribe/subscription-confirmation-email.txt', {'obj': self})
            sender = "lesyeuxouverts@medor.coop"
            recipients = [self.email]
            ## TEMPORARILLY DISABLED
            # send_mail(subject, message, sender, recipients, fail_silently=False)



    def amount(self):
        shipping = 20 if (self.country != "BE" and self.creation_date.date() > date(2015, 1, 20)) else 0
        return 60 + shipping


class Cooperation(TransactionBase):
    """ Describes a cooperation"""
    transaction_type = '02'

    SHARE_CHOICES = (
        (1, '1 (€ 20)'),
        (2, '2 (€ 40)'),
        (3, '3 (€ 60)'),
        (4, '4 (€ 80)'),
        (5, '5 (€ 100)'),
        (6, '6 (€ 120)'),
        (7, '7 (€ 140)'),
        (8, '8 (€ 160)'),
        (9, '9 (€ 180)'),
        (10, '10 (€ 200)'),
        (11, '11 (€ 220)'),
        (12, '12 (€ 240)'),
        (13, '13 (€ 260)'),
        (14, '14 (€ 280)'),
        (15, '15 (€ 300)'),
        (16, '16 (€ 320)'),
        (17, '17 (€ 340)'),
        (18, '18 (€ 360)'),
        (19, '19 (€ 380)'),
        (20, '20 (€ 400)'),
        (50, '50 (€ 1000)')
    )

    share_number = models.PositiveSmallIntegerField('nombre de parts', choices=SHARE_CHOICES, default="1")

    class Meta:
        verbose_name = "part coopérative"
        verbose_name_plural = "parts coopérative"

    __original_status = None

    def __init__(self, *args, **kwargs):
        super(Cooperation, self).__init__(*args, **kwargs)
        self.__original_status = self.status

    def save(self, *args, **kwargs):
        do_send_mail = False

        if self.status != self.__original_status and self.status == 1:
            # If the status has changed and is confirmed, mark for sending a
            # confirmation email
            do_send_mail = True

        super(Cooperation, self).save(*args, **kwargs)
        self.__original_status = self.status

        # Do send the email
        if do_send_mail:
            subject = "Médor SCRL FS. Détails de votre paiement"
            message = render_to_string('subscribe/cooperation-confirmation-email.txt', {'obj': self})
            sender = "lesyeuxouverts@medor.coop"
            recipients = [self.email]
            send_mail(subject, message, sender, recipients, fail_silently=False)


    def amount(self):
        return self.share_number * 20
