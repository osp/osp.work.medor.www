# -*- coding: utf-8 -*-
from django.db import models
from datetime import datetime
from django.db.models import Max


class TransactionBase(models.Model):
    STATUS_CHOICES = (
        (0, u'en cours'),
        (1, u'confirmé'),
        (2, u'annulé')
    )

    COUNTRY_CHOICES = (
        ('BE', u'Belgique'),
        ('FR', u'France'),
        ('LU', u'Luxembourg')
    )

    TITLE_CHOICES = (
        (False, u'Madame'),
        (True, u'Monsieur')
    )

    title = models.BooleanField('civilité', default=False, choices=TITLE_CHOICES)
    first_name = models.CharField('prénom', max_length=30)
    last_name = models.CharField('nom de famille', max_length=30)
    email = models.EmailField('courriel')
    street = models.CharField('rue', max_length=30)
    number = models.CharField('numéro', max_length=10) # 27 bis
    letterbox = models.PositiveSmallIntegerField('boîte postale', max_length=30, null=True, blank=True)
    city = models.CharField('ville', max_length=30)
    zip_code = models.PositiveSmallIntegerField('code postal', max_length=5)
    country = models.CharField('pays', max_length=2, choices=COUNTRY_CHOICES, default="BE")
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.PositiveSmallIntegerField('statut', choices=STATUS_CHOICES, default=0)
    invoice_reference = models.PositiveIntegerField('référence facture', max_length=10, unique=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return u"{} {} {}".format(self.get_title_display(), self.first_name, self.last_name)

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

    def structured_communication(self):
        ref = self.invoice_reference
        nbr = "{}{:02d}".format(ref, ref % 97)
        return "+++{}/{}/{}+++".format(nbr[:3], nbr[3:7], nbr[7:])


class Subscription(TransactionBase):
    """ Describes a cooperation"""
    transaction_type = '01'


class Cooperation(TransactionBase):
    """ Describes a cooperation"""
    transaction_type = '02'

    SHARE_CHOICES = (
        (1, u'1 (€ 20)'),
        (2, u'2 (€ 40)'),
        (3, u'3 (€ 60)'),
        (4, u'4 (€ 80)'),
        (5, u'5 (€ 100)'),
        (6, u'6 (€ 120)'),
        (7, u'7 (€ 140)'),
        (8, u'8 (€ 160)'),
        (9, u'9 (€ 180)'),
        (10, u'10 (€ 200)'),
        (11, u'11 (€ 220)'),
        (12, u'12 (€ 240)'),
        (13, u'13 (€ 260)'),
        (14, u'14 (€ 280)'),
        (15, u'15 (€ 300)'),
        (16, u'16 (€ 320)'),
        (17, u'17 (€ 340)'),
        (18, u'18 (€ 360)'),
        (19, u'19 (€ 380)'),
        (20, u'20 (€ 400)'),
        (50, u'50 (€ 1000)')
    )

    share_number = models.PositiveSmallIntegerField('nombre de parts', choices=SHARE_CHOICES, default="1")
